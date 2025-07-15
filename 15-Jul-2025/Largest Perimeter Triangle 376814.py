# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i+2] + nums[i+1] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0