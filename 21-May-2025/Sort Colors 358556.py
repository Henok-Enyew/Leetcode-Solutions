# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            j = i
            while j > 0 and nums[j] < nums[j - 1]:
                temp = nums[j-1]
                nums[j-1] = nums[j]
                nums[j] = temp
                j-=1