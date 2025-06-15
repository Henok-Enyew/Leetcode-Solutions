# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,sol = [], []

        def backtracking(i):
            if i == len(nums):
                res.append(sol[:])
                return
            backtracking(i+1)

            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()
##
        backtracking(0)
        return res