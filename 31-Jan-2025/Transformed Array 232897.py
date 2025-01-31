# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        if len(nums) == 1:
            return nums
        for i in range(len(nums)):
            if nums[i] == 0:
                result[i] = 0
            elif nums[i] >0:
                j = (i+nums[i]) % len(nums)
                result[i] = nums[j]
            elif nums[i]<0:
                j = abs(i-abs(nums[i])) % len(nums)
                if i >= abs(nums[i]):
                    result[i] = nums[j]
                else:
                    result[i] = nums[-j]
        return result