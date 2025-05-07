# Problem: Find Peak Element - https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)
        low = 0
        high = l-1
        while low <= high:
            index = (high + low) // 2
            if index < l - 1 and  nums[index + 1] > nums[index]:
                low = index + 1
            elif index > 0 and nums[index - 1] > nums[index]:
                high = index - 1
            else:
                return index