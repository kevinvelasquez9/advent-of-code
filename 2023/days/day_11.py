from collections import deque

from abstract_day import AbstractDay


class Day11(AbstractDay):
    def part1(self):
        return self._solve(2)

    def part2(self):
        return self._solve(1000000)

    def _solve(self, cosmic_size):
        grid = [list(line) for line in self.lines]
        R, C = len(grid), len(grid[0])
        galaxies = set()
        big_r = set([r for r in range(R)])
        big_c = set([c for c in range(C)])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "#":
                    galaxies.add((r, c))
                    big_r.discard(r)
                    big_c.discard(c)

        ans = 0
        for r, c in galaxies:
            grid[r][c] = "."
            ans += self._bfs(grid, r, c, big_r, big_c, cosmic_size)
        return ans

    def _bfs(self, grid, r, c, big_r, big_c, cosmic_size):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans, seen, nodes = 0, set(), deque([(r, c, 0)])
        while nodes:
            n = len(nodes)
            for _ in range(n):
                r, c, s = nodes.popleft()
                if (r, c) in seen:
                    continue
                seen.add((r, c))
                ans += s if grid[r][c] == "#" else 0
                for dr, dc in dirs:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < len(grid) and 0 <= cc < len(grid[rr]):
                        d = cosmic_size if rr in big_r or cc in big_c else 1
                        nodes.append((rr, cc, s + d))
        return ans
