from abstract_day import AbstractDay


class Day5(AbstractDay):

    def part1(self):
        data = self.data.split("\n\n")
        seeds = [(int(x), int(x) + 1) for x in data[0].split(": ")[1].split()]
        maps = [[list(map(int, x.split())) for x in m.splitlines()[1:]] for m in data[1:]]

        for m in maps:
            for dest, src, amt in m:
                d = dest - src

    def part2(self):
        pass
