# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col= len(matrix), len(matrix[0])
        l, r = 0,row-1
        res = 0
        while l <= r:
            m = (l+r) // 2
            if target >= matrix[m][0] and target <=  matrix[m][col-1]:
                left , right = 0, col -1
                while left <= right:
                    mid = (left+right) // 2
                    if matrix[m][mid] == target:
                        return True
                    elif target>matrix[m][mid]:
                        left = mid + 1
                    elif target < matrix[m][mid]:
                        right = mid - 1 
                return False
            elif target < matrix[m][0]:
                r = m - 1
            else: 
                l = m + 1
        return False