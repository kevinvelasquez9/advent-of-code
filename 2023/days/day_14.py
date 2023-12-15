from abstract_day import AbstractDay


def roll_north(grid):
    moved = True
    while moved:
        moved = False
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O" and grid[i - 1][j] == ".":
                    grid[i][j], grid[i - 1][j] = ".", "O"
                    moved = True
    return grid


def roll_south(grid):
    moved = True
    while moved:
        moved = False
        for i in range(len(grid) - 2, -1, -1):
            for j in range(len(grid[0])):
                if grid[i][j] == "O" and grid[i + 1][j] == ".":
                    grid[i][j], grid[i + 1][j] = ".", "O"
                    moved = True
    return grid


def roll_west(grid):
    moved = True
    while moved:
        moved = False
        for i in range(len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] == "O" and grid[i][j - 1] == ".":
                    grid[i][j], grid[i][j - 1] = ".", "O"
                    moved = True
    return grid


def roll_east(grid):
    moved = True
    while moved:
        moved = False
        for i in range(len(grid)):
            for j in range(len(grid[0]) - 2, -1, -1):
                if grid[i][j] == "O" and grid[i][j + 1] == ".":
                    grid[i][j], grid[i][j + 1] = ".", "O"
                    moved = True
    return grid


class Day14(AbstractDay):
    def part1(self):
        return 0
        grid = [list(line) for line in self.lines]
        cols = [[grid[r][c] for r in range(len(grid))] for c in range(len(grid[0]))]
        ans = 0
        for col in cols:
            empty = 0
            nw = ["."] * len(col)
            for i in range(len(col)):
                if col[i] == "O":
                    nw[empty] = "O"
                    empty += 1
                if col[i] == "#":
                    nw[i] = "#"
                    empty = i + 1

            for i in range(len(col)):
                if nw[i] == "O":
                    ans += len(col) - i

        return ans

    def part2(self):
        grid = [list(line) for line in self.lines]
        dp = {}

        k = []
        for row in grid:
            k.append("".join(row))
        k = "\n".join(k)
        dp[k] = 0

        start = 0
        cycle = None
        for _ in range(1000000000):
            start += 1
            grid = roll_north(grid)
            grid = roll_west(grid)
            grid = roll_south(grid)
            grid = roll_east(grid)
            k = []
            for row in grid:
                k.append("".join(row))
            k = "\n".join(k)
            if k in dp:
                cycle = start - dp[k]
                break
            dp[k] = start

        print(f"cycles: {cycle}")

        for _ in range((1000000000 - start) % cycle):
            grid = roll_north(grid)
            grid = roll_west(grid)
            grid = roll_south(grid)
            grid = roll_east(grid)

        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "O":
                    ans += len(grid[r]) - r
        return ans
