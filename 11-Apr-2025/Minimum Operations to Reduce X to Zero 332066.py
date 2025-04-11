# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        l = 0
        sm = 0
        max_w = -1
        for r in range(n):
            sm += nums[r]
            while sm > target and l <= r:
                sm -= nums[l]
                l += 1
            if sm == target:
                max_w = max(max_w, r- l + 1)
        return -1 if max_w == -1 else n - max_w 
            