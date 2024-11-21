from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for guard in guards:
            grid[guard[0]][guard[1]] = 1
        for wall in walls:
            grid[wall[0]][wall[1]] = 2
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def mark_guarded(row, col, drow, dcol):
            r, c = row, col
            while 0 <= r < m and 0 <= c < n:
                if grid[r][c] in (1, 2):
                    break
                if grid[r][c] == 0:
                    grid[r][c] = -1
                r += drow
                c += dcol
        for guard in guards:
            for drow, dcol in directions:
                mark_guarded(guard[0] + drow, guard[1] + dcol, drow, dcol)
        unguarded_count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:  
                    unguarded_count += 1
        return unguarded_count
