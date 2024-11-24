from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs = float('inf')
        negative_count = 0

        # Iterate through the matrix
        for row in matrix:
            for num in row:
                # Add the absolute value of the current element to the total sum
                total_sum += abs(num)
                # Track the smallest absolute value
                min_abs = min(min_abs, abs(num))
                # Count negatives
                if num < 0:
                    negative_count += 1

        # If the number of negatives is odd, subtract twice the smallest absolute value
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs

        return total_sum
