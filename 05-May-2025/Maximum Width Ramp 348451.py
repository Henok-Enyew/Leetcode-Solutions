# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        length = len(nums)
        max_arr = [0] * length
        i = length - 1
        prev_max = 0
        for n in reversed(nums):
            max_arr[i] = max(n, prev_max)
            prev_max = max_arr[i]
            i-=1
        print(max_arr)

        res = 0
        l = 0
        for i in range(length):
            if nums[l] <= max_arr[i]:
                res = max(res, i - l)
            else:
                while nums[l] > max_arr[i]:
                    l += 1

        return res