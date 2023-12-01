from abstract_day import AbstractDay


class Day1(AbstractDay):
    def __init__(self):
        super().__init__(2023, 1)

    def part1(self):
        total = 0
        for line in self.lines:
            num = ""
            for c in line:
                if c.isdigit():
                    num += c
            total += int(num[0] + num[-1])
        return total

    def part2(self):
        words = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }
        words_lens = [3, 4, 5]

        total = 0
        for line in self.lines:
            num = ""
            for i, c in enumerate(line):
                if c.isdigit():
                    num += c
                for w_len in words_lens:
                    if i + w_len <= len(line) and line[i:i + w_len] in words:
                        num += words[line[i:i + w_len]]
            total += int(num[0] + num[-1])
        return total
