# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if i < len(nums) and nums[i] == val:
                del nums[i] 
            else:
                i += 1
        return len(nums)