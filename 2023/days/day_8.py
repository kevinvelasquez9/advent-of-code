from math import lcm
from re import findall

from abstract_day import AbstractDay


class Day8(AbstractDay):
    def part1(self):
        return self._solve(3)

    def part2(self):
        return self._solve(1)

    def _solve(self, num_end_with):
        d = [c for c in self.lines[0]]
        m = {node: (l, r) for node, l, r in [findall(r"\b\w+\b", line) for line in self.lines[2:]]}
        steps = d_i = 0

        nodes = [node for node in m.keys() if node.endswith(num_end_with * "A")]
        steps_needed = [0] * len(nodes)

        while True:
            if 0 not in steps_needed:
                return lcm(*steps_needed)

            for i, node in enumerate(nodes):
                if node.endswith(num_end_with * "Z"):
                    steps_needed[i] = steps

            nodes = [m[node][0] if d[d_i] == "L" else m[node][1] for node in nodes]
            steps, d_i = steps + 1, (d_i + 1) % len(d)
