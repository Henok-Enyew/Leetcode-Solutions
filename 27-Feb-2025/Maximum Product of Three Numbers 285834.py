# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        upper = nums[l-1] * nums[l-2] * nums[l-3] 
        lower = nums[l-1] * nums[0] * nums[1]
        return lower if lower > upper else upper 