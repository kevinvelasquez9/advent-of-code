from abstract_day import AbstractDay


def _get_num_hits(line):
    hits = 0
    _, s = line.split(": ")
    s = ' '.join(s.split())
    wins, nums = s.split(" | ")
    wins = set(wins.split(" "))
    for n in nums.split(" "):
        if n in wins:
            hits += 1
    return hits


class Day4(AbstractDay):
    def part1(self):
        total = 0
        for line in self.lines:
            hits = _get_num_hits(line)
            if hits > 0:
                total += 2 ** (hits - 1)
        return total

    def part2(self):
        copies = [1] * len(self.lines)
        for i, line in enumerate(self.lines):
            hits = _get_num_hits(line)
            for j in range(hits):
                copies[i + j + 1] += copies[i]
        return sum(copies)
