class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[len(t) - 1]