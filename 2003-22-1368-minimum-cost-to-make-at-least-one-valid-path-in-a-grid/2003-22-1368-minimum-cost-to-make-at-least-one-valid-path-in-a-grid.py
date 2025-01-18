from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        costs = [[float('inf')] * n for _ in range(m)]
        costs[0][0] = 0
        dq = deque([(0, 0, 0)])

        while dq:
            cost, x, y = dq.popleft()
            if cost > costs[x][y]:
                continue
            for i, (dx, dy) in enumerate(directions, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + (grid[x][y] != i)
                    if new_cost < costs[nx][ny]:
                        costs[nx][ny] = new_cost
                        if grid[x][y] == i:
                            dq.appendleft((new_cost, nx, ny))
                        else:
                            dq.append((new_cost, nx, ny))
        return costs[m - 1][n - 1]
