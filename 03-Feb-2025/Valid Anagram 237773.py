# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss = list(s)
        tt = list(t)
        ss.sort()
        tt.sort()
        for i in range(len(s)):
            if ss[i] != tt[i]:
                return False
        return True