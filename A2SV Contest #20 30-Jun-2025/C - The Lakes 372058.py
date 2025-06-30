# Problem: C - The Lakes - https://codeforces.com/gym/618729/problem/C

import sys
from collections import deque

input = sys.stdin.read().split()
ptr = 0
t = int(input[ptr])
ptr += 1
for _ in range(t):
    n, m = map(int, input[ptr:ptr+2])
    ptr += 2
    grid = []
    for _ in range(n):
        row = list(map(int, input[ptr:ptr+m]))
        ptr += m
        grid.append(row)
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    max_volume = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                volume = 0
                
                while stack:
                    x, y = stack.pop()
                    volume += grid[x][y]
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if grid[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                
                max_volume = max(max_volume, volume)
    
    print(max_volume)