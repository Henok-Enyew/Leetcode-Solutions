# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while queue:
            row, col, steps = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if (0 <= new_row < rows
                    and 0 <= new_col < cols
                    and maze[new_row][new_col] == "."):
                    if (new_row == 0
                    or new_row == rows - 1
                    or new_col == 0 or new_col == cols - 1):
                        return steps + 1
                    
                    maze[new_row][new_col] = "+"
                    queue.append((new_row, new_col, steps + 1))
        
        return -1
        