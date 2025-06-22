# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        minVal = float('inf')
        def backtrack(ind, path):
            nonlocal minVal
            if ind >= len(cookies):
                maxNum = max(path)
                if maxNum < minVal:
                    minVal = maxNum
                return
            if max(path) > minVal:
                return

            for i in range(k):
                path[i] += cookies[ind]
                backtrack(ind+1, path)
                path[i] -= cookies[ind]

        backtrack(0,[0]*k)
        return minVal