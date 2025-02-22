# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 1:
            return mat[0]
        array = []
        row,col = len(mat),len(mat[0])
        i,j=0,0

        while 0<= i<row and 0<= j<col:
            while i>=0 and j<col:
                # print(i,j)
                array.append(mat[i][j])
                i-=1
                j+=1
            i+=1
            if j == col:
                i+=1    
                j-=1
            # print("AAAAAAAAAA")
            while i<row and j>=0:
                # print(i,j)
                array.append(mat[i][j])
                j-=1
                i+=1
            j+=1
            if i == row:
                i-=1    
                j+=1
            # print(array)
            # print("Final- ", i,j)
        # array.append(mat[row-1][col-1])
        return array