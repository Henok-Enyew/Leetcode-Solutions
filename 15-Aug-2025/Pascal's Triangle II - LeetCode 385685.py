# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRow = rowIndex + 1
        dp = [[1], [1,1]]
        if numRow < 3:
            return dp[rowIndex]
        for i in range(2,numRow):
            newarr = [dp[i-1][0]]
            for j in range(len(dp[i-1]) -1):
                newarr.append( dp[i-1][j] + dp[i-1][j+1])
            newarr.append(dp[i-1][-1])
            dp.append(newarr)
        return dp[rowIndex]