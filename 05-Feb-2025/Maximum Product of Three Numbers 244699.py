# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l=len(nums) 
        prod1 = nums[l-1] * nums[l-2] * nums[l-3]
        prod2= nums[l-1] * nums[0] * nums[1]        
        prod3= nums[2] * nums[0] * nums[1]
        return max(prod1,prod2,prod3)
