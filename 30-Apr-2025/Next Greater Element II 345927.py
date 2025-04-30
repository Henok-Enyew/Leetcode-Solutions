# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            cur_index = i % n
            while stack and nums[cur_index] > nums[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = nums[cur_index]
            if i < n:
                stack.append(cur_index)
        
        return res
