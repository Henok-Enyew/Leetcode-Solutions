# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

# from collections import defaultdict
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        directions = {1: [(0,-1),(0,1)],
                    2: [(-1,0),(1,0)],
                    3: [(0,-1),(1,0)],
                    4: [(0,1),(1,0)],
                    5: [(0,-1),(-1,0)],
                    6: [(0,1),(-1,0)]}
        visited = set([(0,0)])

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def dfs(row,col):
            if row == len(grid) - 1 and col == len(grid[0])-1:
                return True

            for row_change, col_change in directions[grid[row][col]]:
                new_row = row + row_change
                new_col = col + col_change
                if (inbound(new_row, new_col) and
                (new_row, new_col) not in visited and
                (-row_change, -col_change) in
                directions[grid[new_row][new_col]]):
                    visited.add((new_row, new_col))
                    found = dfs(new_row, new_col)
                    if found:
                        return True
            return False
        return dfs(0,0)