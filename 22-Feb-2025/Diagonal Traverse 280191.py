# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        array = []
        row,col = len(mat),len(mat[0])
        i,j=0,0

        while 0<= i<row and 0<= j<col:
            while i>=0 and j<col:
                array.append(mat[i][j])
                i-=1
                j+=1
            i+=1
            if j == col:
                i+=1    
                j-=1
            while i<row and j>=0:
                array.append(mat[i][j])
                j-=1
                i+=1
            j+=1
            if i == row:
                i-=1    
                j+=1
        return array