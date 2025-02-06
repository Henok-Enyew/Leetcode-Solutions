# Problem: Dota2 Senate - https://leetcode.com/problems/dota2-senate/

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque()
        D = deque()
        n = len(senate)
        
        for i, s in enumerate(senate):
            if s == 'R':
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            r = R.popleft()
            d = D.popleft()
            if r < d:
                R.append(r + n)
            else:
                D.append(d + n)
        
        return "Radiant" if R else "Dire"
