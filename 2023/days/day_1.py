from abstract_day import AbstractDay


class Day1(AbstractDay):
    def __init__(self):
        super().__init__(2023, 1)

    def part1(self):
        total = 0
        for line in self.lines:
            digits = []
            for c in line:
                if c.isdigit():
                    digits.append(c)
            total += int(digits[0] + digits[-1])
        return total

    def part2(self):
        words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        total = 0
        for line in self.lines:
            digits = []
            for i, c in enumerate(line):
                if c.isdigit():
                    digits.append(c)
                for j, word in enumerate(words):
                    if line[i:].startswith(word):
                        digits.append(str(j + 1))
            total += int(digits[0] + digits[-1])
        return total
