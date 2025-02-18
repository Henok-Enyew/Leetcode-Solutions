# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current = 0
        max_distance = 0
        obs = set()

        for x, y in obstacles:
            obs.add((x, y))

        x, y = 0, 0
        for c in commands:
            if c == -2:
                current = (current + 3) % 4
            elif c == -1:
                current = (current + 1) % 4
            else:
                dx, dy = directions[current]
                for _ in range(c):
                    nx, ny = x + dx, y + dy

                    if (nx, ny) in obs:
                        break

                    x, y = nx, ny
                    max_distance = max(max_distance, x * x + y * y)

        return max_distance
