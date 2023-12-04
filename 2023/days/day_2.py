from abstract_day import AbstractDay


def _max_color_counts(sets) -> tuple[int, int, int]:
    mr = mg = mb = 0
    for s in sets.split("; "):
        m = {"red": 0, "green": 0, "blue": 0}
        for draw in s.split(", "):
            amt, color = draw.split(" ")
            m[color] += int(amt)
        mr, mg, mb = max(mr, m["red"]), max(mg, m["green"]), max(mb, m["blue"])
    return mr, mg, mb


class Day2(AbstractDay):
    def part1(self):
        total = 0
        for line in self.lines:
            game, sets = line.split(": ")
            game = int(game.split(" ")[-1])
            mr, mg, mb = _max_color_counts(sets)
            total += game if mr <= 12 and mg <= 13 and mb <= 14 else 0
        return total

    def part2(self):
        total = 0
        for line in self.lines:
            _, sets = line.split(": ")
            mr, mg, mb = _max_color_counts(sets)
            total += mr * mg * mb
        return total
