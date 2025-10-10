# Problem: Maximum Number of Operations With the Same Score II - https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        maxOperations = 0
        length = len(nums)
        memoization = [[0] * length for _ in range(length)]
        start = 0
        end = length - 1

        maxOperations = max(maxOperations, self.findMaxOpsHelper(nums, start + 2, end, nums[start] + nums[start + 1], memoization) + 1)
        maxOperations = max(maxOperations, self.findMaxOpsHelper(nums, start + 1, end - 1, nums[start] + nums[end], memoization) + 1)
        maxOperations = max(maxOperations, self.findMaxOpsHelper(nums, start, end - 2, nums[end] + nums[end - 1], memoization) + 1)

        return maxOperations

    def findMaxOpsHelper(self, nums: List[int], left: int, right: int, previousSum: int, memoization: List[List[int]]) -> int:
        if left >= right:
            return 0
        if memoization[left][right] != 0:
            return memoization[left][right]

        maxOps = 0
        if nums[left] + nums[left + 1] == previousSum:
            maxOps = max(maxOps, self.findMaxOpsHelper(nums, left + 2, right, previousSum, memoization) + 1)
        if nums[left] + nums[right] == previousSum:
            maxOps = max(maxOps, self.findMaxOpsHelper(nums, left + 1, right - 1, previousSum, memoization) + 1)
        if nums[right] + nums[right - 1] == previousSum:
            maxOps = max(maxOps, self.findMaxOpsHelper(nums, left, right - 2, previousSum, memoization) + 1)

        memoization[left][right] = maxOps
        return maxOps