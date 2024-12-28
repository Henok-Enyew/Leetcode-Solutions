from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Step 1: Compute sums of all windows of size k
        window_sums = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        window_sums[0] = current_sum
        for i in range(1, n - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            window_sums[i] = current_sum
        
        # Step 2: Compute left and right arrays
        left = [0] * len(window_sums)
        best_left = 0
        for i in range(len(window_sums)):
            if window_sums[i] > window_sums[best_left]:
                best_left = i
            left[i] = best_left

        right = [0] * len(window_sums)
        best_right = len(window_sums) - 1
        for i in range(len(window_sums) - 1, -1, -1):
            if window_sums[i] >= window_sums[best_right]:  # >= ensures lexicographical order
                best_right = i
            right[i] = best_right

        # Step 3: Find the maximum sum of three subarrays
        max_sum = 0
        result = [-1, -1, -1]
        for middle in range(k, len(window_sums) - k):
            l = left[middle - k]
            r = right[middle + k]
            total = window_sums[l] + window_sums[middle] + window_sums[r]
            if total > max_sum:
                max_sum = total
                result = [l, middle, r]

        return result
