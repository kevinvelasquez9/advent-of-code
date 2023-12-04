from abstract_day import AbstractDay


class Day1(AbstractDay):
    def part1(self):
        dirs = {"(": 1, ")": - 1}
        return sum([dirs[c] for c in self.data])

    def part2(self):
        dirs = {"(": 1, ")": - 1}
        floor = 0
        for i, c in enumerate(self.data):
            floor += dirs[c]
            if floor < 0:
                return i + 1
