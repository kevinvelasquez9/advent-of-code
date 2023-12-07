from hashlib import md5

from abstract_day import AbstractDay


class Day4(AbstractDay):
    def part1(self):
        return self._solve(5)

    def part2(self):
        return self._solve(6)

    def _solve(self, num_zeroes: int) -> int:
        ans, zeroes = 1, num_zeroes * "0"
        while True:
            h = md5(f"{self.data}{ans}".encode()).hexdigest()
            if h.startswith(zeroes):
                return ans
            ans += 1
