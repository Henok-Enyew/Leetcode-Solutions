# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums, target):
        memo = {}
        def dfs(remain):
            if remain == 0:
                return 1
            if remain in memo:
                return memo[remain]
            count = 0
            for num in nums:
                if num <= remain:
                    count += dfs(remain - num)
            memo[remain] = count
            return count
        return dfs(target)