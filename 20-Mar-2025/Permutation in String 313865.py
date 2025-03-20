# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = collections.Counter(s1)
        N = len(s2)
        memo = len(s1)
        right = 0
        while right + memo <= N:
            if s2[right] in mp:
                mp2 = collections.Counter(s2[right:right+memo])
                if mp == mp2:
                    return True
            right+=1
        return False