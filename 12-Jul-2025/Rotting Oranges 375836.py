# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid) -> int:
        q = deque()
        tim, fresh = 0, 0
        n, m = len(grid), len(grid[0])
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        
        directions = [[-1,0], [0,1], [1,0], [0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for x,y in directions:
                    nr, nc = r+x, y+c
                    if (nr < 0 or nr >= n or nc < 0 or nc >= m or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append([nr,nc])
                    fresh -=1
            tim += 1
        
        return tim if fresh == 0 else -1