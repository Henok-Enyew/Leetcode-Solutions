# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0
        while target > 1:
            
            if maxDoubles > 0:
                if target % 2:
                    steps += 1
                    target -= 1
                else:
                    steps += 1
                    target //= 2
                    maxDoubles -= 1
            else:
                steps += target - 1
                target -= target - 1
        return steps
