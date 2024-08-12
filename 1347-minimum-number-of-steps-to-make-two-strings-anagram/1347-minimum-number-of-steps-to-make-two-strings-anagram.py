class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS = collections.Counter(s)
        countT = collections.Counter(t)
        return sum((countT - countS).values())
