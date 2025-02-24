# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row , col= len(matrix), len(matrix[0])  
        for i in range(row):
            if 0 in matrix[i]:
                for index, el in enumerate(matrix[i]):
                    if el == 0:
                        for k in range(row):
                            if matrix[k][index] !=0: 
                                matrix[k][index] = float('-inf')
                for j in range(col):
                    matrix[i][j] = float('-inf')
        print(matrix)
        for k in range(row):
            for j in range(col):
                if matrix[k][j] == float('-inf'):
                    matrix[k][j] = 0
                