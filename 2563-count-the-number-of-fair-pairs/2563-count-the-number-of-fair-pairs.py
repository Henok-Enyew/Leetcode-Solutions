from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        for i in range(n):
            left_bound = lower - nums[i]  
            right_bound = upper - nums[i]  
            
            left_index = bisect_left(nums, left_bound, i + 1)  
            right_index = bisect_right(nums, right_bound, i + 1)
            
            count += right_index - left_index
        
        return count
