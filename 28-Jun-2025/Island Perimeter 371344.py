# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        perimeter = 0
        def dfs(grid, visited, row, col):
            nonlocal perimeter
            # base case
            if row >= len(grid) and col >= len(grid[0]):
                return
            if grid[row][col] == 1:
                if not inbound(row+1,col) or grid[row+1][ col] == 0:
                    perimeter += 1
                if not inbound(row-1,col) or grid[row-1][ col] == 0:
                    perimeter += 1
                if not inbound(row,col+1) or grid[row][col+1] == 0:
                    perimeter += 1
                if not inbound(row,col-1) or grid[row][col-1] == 0:
                    perimeter += 1
            visited[row][col] = True
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    dfs(grid, visited, new_row, new_col)
        dfs(grid, visited,0,0)
        return perimeter