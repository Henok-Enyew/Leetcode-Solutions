from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(r, c, index):
            stack = [(r, c)]
            grid[r][c] = index
            size = 0
            while stack:
                x, y = stack.pop()
                size += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = index
                        stack.append((nx, ny))
            return size
        
        area = {}
        index = 2
        max_area = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[index] = dfs(i, j, index)
                    max_area = max(max_area, area[index])
                    index += 1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            seen.add(grid[ni][nj])
                    max_area = max(max_area, 1 + sum(area[idx] for idx in seen))
        
        return max_area
