from abstract_day import AbstractDay


def _explore(grid, r, c) -> tuple[int, int]:
    part1 = 0
    hits = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            rr, cc = r + dr, c + dc
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[rr]) and grid[rr][cc].isdigit():
                part_num = _get_part_num(grid[rr], cc)
                part1 += part_num
                hits.append(part_num)
    part2 = hits[0] * hits[1] if len(hits) == 2 else 0
    return part1, part2


def _get_part_num(row, c) -> int:
    row_ = row.copy()
    left = right = c
    while left > 0 and row[left - 1].isdigit():
        left -= 1
        row[left] = '.'
    while right < len(row) - 1 and row[right + 1].isdigit():
        right += 1
        row[right] = '.'
    return int(''.join(row_[left:right + 1]))


class Day3(AbstractDay):
    def part1(self):
        total, _ = self._solve()
        return total

    def part2(self):
        _, total = self._solve()
        return total

    def _solve(self):
        part1 = part2 = 0
        grid = [[c for c in line] for line in self.lines]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if not grid[r][c].isdigit() and grid[r][c] != '.':
                    d1, d2 = _explore(grid, r, c)
                    part1, part2 = part1 + d1, part2 + d2
        return part1, part2
