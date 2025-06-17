# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        def backtracking(i, subset):
            if i == len(nums):
                subsets.append(subset[:])
                return 
            
            subset.append(nums[i])
            backtracking(i+1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtracking(i+1, subset)
        backtracking(0,[])
        return subsets