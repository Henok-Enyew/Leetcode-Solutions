from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Flatten the board into a list
        start = tuple(board[0] + board[1])  # Use a tuple for immutability
        goal = (1, 2, 3, 4, 5, 0)
        
        # Define valid moves for each index
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        # BFS setup
        queue = deque([(start, start.index(0), 0)])  # (state, index of 0, moves)
        visited = set()
        visited.add(start)
        
        # BFS loop
        while queue:
            state, zero_pos, steps = queue.popleft()
            
            # Check if we've reached the goal
            if state == goal:
                return steps
            
            # Explore all valid moves
            for neighbor in moves[zero_pos]:
                new_state = list(state)
                # Swap 0 with the neighbor
                new_state[zero_pos], new_state[neighbor] = new_state[neighbor], new_state[zero_pos]
                new_tuple = tuple(new_state)
                
                # Add new state to queue if not visited
                if new_tuple not in visited:
                    visited.add(new_tuple)
                    queue.append((new_tuple, neighbor, steps + 1))
        
        # If no solution is found
        return -1
