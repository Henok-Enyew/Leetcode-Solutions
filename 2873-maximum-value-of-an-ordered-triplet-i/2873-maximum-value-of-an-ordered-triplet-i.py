from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = 0
        n = len(nums)

        max_i = nums[0]
        max_diff = float('-inf')

        for j in range(1, n - 1):
            max_diff = max(max_diff, max_i - nums[j])
            max_i = max(max_i, nums[j])
            max_value = max(max_value, max_diff * nums[j + 1])

        return max_value
