from abstract_day import AbstractDay


class Day2(AbstractDay):
    def part1(self):
        paper = 0
        for line in self.lines:
            l, w, h = [int(n) for n in line.split("x")]
            slack = min(l * w, l * h, w * h)
            paper += 2 * l * w + 2 * w * h + 2 * h * l + slack
        return paper

    def part2(self):
        ribbon = 0
        for line in self.lines:
            l, w, h = [int(n) for n in line.split("x")]
            perimeter = 2 * min(l + w, l + h, w + h)
            ribbon += l * w * h + perimeter
        return ribbon
