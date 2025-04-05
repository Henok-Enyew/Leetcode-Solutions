class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, curr):
            if i == len(nums):
                return curr
            return dfs(i + 1, curr) + dfs(i + 1, curr ^ nums[i])
        return dfs(0, 0)
