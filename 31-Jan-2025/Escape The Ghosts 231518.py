# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        for ghost in ghosts:
            x = target[0] - ghost[0]
            y = target[1] - ghost[1]
            if abs(x)+abs(y)<= abs(target [0]) + abs(target[1]):
                return False 
        return True