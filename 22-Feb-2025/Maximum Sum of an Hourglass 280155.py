# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        max_val = 0
        for i in range(row-2):
            val = 0
            for j in range(col-2):
                for k in range(j,j+3):
                    print(i,k)
                    val += grid[i][k]
                    val += grid[i+2][k]
                print("AAAAA")
                val+=grid[i+1][j+1]
                print(val)
                max_val = max(max_val,val)
                val = 0
        return max_val