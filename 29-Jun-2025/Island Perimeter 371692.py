# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        perimeter = 0
# 
        def dfs(r, c):
            nonlocal perimeter
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                perimeter += 1
                return
            if visited[r][c]:
                return
            visited[r][c] = True
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return perimeter 

        return 0