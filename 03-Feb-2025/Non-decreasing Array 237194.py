# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        ischanged = False
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            elif ischanged:
                return False
            if i==0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            ischanged = True
        return True