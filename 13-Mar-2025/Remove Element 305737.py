# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = float('inf')
                count-=1
        nums.sort()
        return count