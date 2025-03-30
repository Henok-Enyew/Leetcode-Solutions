# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                sm = matrix[i][j]
                if i > 0:
                    sm += self.prefix_sum[i-1][j]
                if j > 0:
                    sm += self.prefix_sum[i][j-1]
                if i > 0 and j > 0:
                    sm -= self.prefix_sum[i-1][j-1] 
                self.prefix_sum[i][j] = sm

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix_sum[row2][col2]
        # we will check each case
        if row1 > 0:
            total -= self.prefix_sum[row1-1][col2]
        if col1 > 0:
            total -= self.prefix_sum[row2][col1-1]
        if row1 > 0 and col1 > 0:
            total += self.prefix_sum[row1-1][col1-1]   
        return total
