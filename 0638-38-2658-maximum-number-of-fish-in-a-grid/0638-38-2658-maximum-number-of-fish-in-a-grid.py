from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] > 0:
                fish = grid[r][c]
                grid[r][c] = 0
                return fish + sum(dfs(r + dr, c + dc) for dr, dc in directions)
            return 0

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return max((dfs(r, c) for r in range(m) for c in range(n) if grid[r][c] > 0), default=0)
