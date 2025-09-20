# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        def valid(row, col):
            tl,tr = float('inf'), float('inf')
            if col > 0:
                tl = matrix[row-1][col-1]
            if col < n-1:
                tr = matrix[row-1][col+1]
            
            du = matrix[row-1][col]

            return min(tl,tr,du)
        for row in range(1, m):
            for col in range(n):

                matrix[row][col] += valid(row,col)        
        return min(matrix[m-1])
