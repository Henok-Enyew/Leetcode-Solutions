# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        current = []
        def backtracking(indx):
            if len(current) >= 2:
                for i in range(1,len(current)):
                    if current[i-1] - current[i] != 1:
                        return False
                if indx >= len(s):
                    return True
                
            for i in range(indx, len(s)):
                current.append(int(s[indx:i+1]))
                if backtracking(i+1):
                    return True
                current.pop()
            return False
        
        return backtracking(0)

