# Problem: Find Peak Element - https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)
        low = 0
        high = l-1
        index = 0
        if l == 1:
            return 0
        elif l == 2:
            return 0 if nums[0] > nums[1] else 1
        while low <= high:
            index = (high + low) // 2
            b = nums[index - 1] if index - 1 >= 0 else float('-inf')
            t = nums[index + 1] if index + 1 < l else float('-inf')
            if nums[index] > t and nums[index] > b:
                return index
            elif nums[index + 1] > nums[index]:
                low = index + 1
            elif nums[index - 1] > nums[index]:
                high = index - 1