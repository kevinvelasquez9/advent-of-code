from abstract_day import AbstractDay


def _houses_seen(moves) -> set[tuple[int, int]]:
    dirs = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}
    x = y = 0
    seen = set()
    for c in moves:
        seen.add((x, y))
        dx, dy = dirs[c]
        x, y = x + dx, y + dy
        seen.add((x, y))
    return seen


class Day3(AbstractDay):
    def part1(self):
        return len(_houses_seen(self.data))

    def part2(self):
        santa, robo = self.data[0::2], self.data[1::2]
        return len(_houses_seen(santa).union(_houses_seen(robo)))
