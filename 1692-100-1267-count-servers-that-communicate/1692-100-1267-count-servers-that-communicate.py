from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_count, col_count = [0] * m, [0] * n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    count += 1
        
        return count
