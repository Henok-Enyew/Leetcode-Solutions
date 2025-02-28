# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = matrix[0]
        col=0
        while col<len(matrix[0]):
            c = col
            row=0
            val = matrix[row][col]
            while row<len(matrix) and c < len(matrix[0]):
                if matrix[row][c] != val:
                    return False
                row+=1
                c+=1
            col+=1
        row = 1
        print("hala")
        while row<len(matrix):
            r = row
            col = 0  
            val = matrix[r][col]
            while col < len(matrix[0]) and r < len(matrix):
                print(matrix[r][col] ,val)
                if matrix[r][col] != val:
                    return False
                col+=1
                r+=1
            row+=1
        return True 