# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        i = 0
        j = 0
        while i < len(haystack):
            ans = i
            while i < len(haystack) and haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return ans
            i = ans + 1
            j = 0
        return -1
        