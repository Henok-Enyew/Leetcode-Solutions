# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for st in t:
            if i < len(s) and st == s[i]:
                i +=1
        return i == len(s) 