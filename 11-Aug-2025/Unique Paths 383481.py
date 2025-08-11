# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1

        def defaultorVal(i,j):
            if 0 <= i < m and 0 <= j < n:
                return dp[i][j]
            return 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    continue 
                dp[i][j] = defaultorVal(i + 1,j) + defaultorVal(i ,j + 1)
        return dp[0][0]