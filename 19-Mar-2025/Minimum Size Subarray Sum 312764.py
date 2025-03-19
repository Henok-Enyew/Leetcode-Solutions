# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowSum = 0
        minLen = len(nums) + 1
        left = 0
        right = 0
        while right < len(nums):
            windowSum += nums[right]
            while windowSum >= target and left<=right:
                minLen = min(minLen, right - left + 1)
                windowSum -= nums[left]
                left += 1
            if windowSum < target:
                right+=1
        return minLen if minLen <= len(nums) else 0