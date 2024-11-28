from collections import deque
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque([(0, 0, 0)])  # (cost, row, col)
        while dq:
            cost, x, y = dq.popleft()
            if x == m - 1 and y == n - 1:
                return cost
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        if grid[nx][ny] == 0:
                            dq.appendleft((new_cost, nx, ny))  
                        else:
                            dq.append((new_cost, nx, ny))  # Add to the back if obstacle
        return -1  # Should never reach here
