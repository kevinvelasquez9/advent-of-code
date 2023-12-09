from abstract_day import AbstractDay


class Day9(AbstractDay):
    def part1(self):
        return self._solve(False)

    def part2(self):
        return self._solve(True)

    def _solve(self, reverse):
        ans = 0
        for line in self.lines:
            orig_nums = [int(x) for x in line.split()]
            orig_nums = orig_nums[::-1] if reverse else orig_nums
            diffs = [orig_nums.copy()]
            while sum(diffs[-1]) != 0:
                last, new = diffs[-1], []
                new = [last[i + 1] - last[i] for i in range(len(last) - 1)]
                diffs.append(new)
            ans += sum([diff[-1] for diff in diffs])
        return ans
