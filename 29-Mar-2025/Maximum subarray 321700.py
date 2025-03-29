# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum