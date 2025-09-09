# Problem: Number of Closed Islands - https://leetcode.com/problems/number-of-closed-islands/

from typing import List
from collections import deque

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:  # found land
                    grid[i][j] = 1   # mark visited
                    q = deque([(i, j)])
                    touches_border = False

                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if grid[nr][nc] == 0:
                                    grid[nr][nc] = 1
                                    q.append((nr, nc))
                            else:
                                touches_border = True

                    if not touches_border:
                        ans += 1

        return ans