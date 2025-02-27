# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        row,col = len(matrix),len(matrix[0])
        sm = 0
        count_negatives = 0
        min_val = float('inf')
        for r in range(row):
            for c in range(col):
                min_val = min(min_val,abs(matrix[r][c]))
                if matrix[r][c] <= 0:
                    count_negatives+=1
                    sm+=abs(matrix[r][c])
                else:
                    sm+=matrix[r][c]
        if count_negatives %2 == 1:
            sm -= (min_val*2) 
        return sm  

