from abstract_day import AbstractDay


class Day13(AbstractDay):
    def part1(self):
        return self._solve(0)

    def part2(self):
        return self._solve(1)

    def _solve(self, d):
        ps = self.data.split("\n\n")
        ans = 0
        for p in ps:
            rows = [list(line) for line in p.splitlines()]
            cols = [[rows[r][c] for r in range(len(rows))] for c in range(len(rows[0]))]
            # look for vertical reflection
            for c in range(len(rows[0]) - 1):
                if d == sum(self._num_diff(row, c, c + 1) for row in rows):
                    ans += (c + 1)
            # look for horizontal reflection
            for r in range(len(rows) - 1):
                if d == sum(self._num_diff(col, r, r + 1) for col in cols):
                    ans += (r + 1) * 100
        return ans

    def _num_diff(self, arr, i, j):
        d = 0
        while i >= 0 and j < len(arr):
            if arr[i] != arr[j]:
                d += 1
            i -= 1
            j += 1
        return d
