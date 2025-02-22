# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r= 0,len(matrix)-1
        while l<r:
            for j in range(r-l):
                t,b = l,r
                temp = matrix[t][l+j]
                matrix[t][l+j] = matrix[b-j][l]
                matrix[b-j][l] = matrix[b][r-j]
                matrix[b][r-j] = matrix[t+j][r]
                matrix[t+j][r] = temp
            l+=1
            r-=1