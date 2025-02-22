# Problem: Maximum Sum of an Hourglass - LeetCode - https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        max_val = 0
        for i in range(row-2):
            val = 0
            for j in range(col-2):
                for k in range(j,j+3):
                    val += grid[i][k]
                    val += grid[i+2][k]
                val+=grid[i+1][j+1]
                max_val = max(max_val,val)
                val = 0
        return max_val