class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            lcp = ''
            strs.sort()
            i = 0
            l1 = len(strs[0])
            while i<l1 and strs[0][i] == strs[-1][i]:
                lcp+=strs[0][i]
                i+=1
            return lcp