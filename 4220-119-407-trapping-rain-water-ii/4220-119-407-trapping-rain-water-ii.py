from heapq import heappush, heappop
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        water_trapped = 0
        
        # Add all boundary cells to the heap
        for i in range(m):
            for j in (0, n - 1):  # First and last columns
                heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in (0, m - 1):  # First and last rows
                heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        
        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Process the heap
        while heap:
            height, x, y = heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # Water trapped if the current cell height > neighbor height
                    water_trapped += max(0, height - heightMap[nx][ny])
                    # Update neighbor height to maintain the boundary
                    heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True
        
        return water_trapped
