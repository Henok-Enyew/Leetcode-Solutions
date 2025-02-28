class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        from functools import lru_cache
        
        @lru_cache(None)
        def lcs(i, j):
            if i == len(str1) or j == len(str2):
                return ""
            if str1[i] == str2[j]:
                return str1[i] + lcs(i + 1, j + 1)
            left, right = lcs(i + 1, j), lcs(i, j + 1)
            return left if len(left) > len(right) else right
        
        lcs_str, i, j, res = lcs(0, 0), 0, 0, ""
        for c in lcs_str:
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1
        
        return res + str1[i:] + str2[j:]
