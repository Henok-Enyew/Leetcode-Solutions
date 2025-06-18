# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(ind):
            res = []
            if ind == len(nums):
                return [[]]
            perms = backtracking(ind+1)
            for perm in perms:
                for j in range(len(perm) + 1):
                    permCopy = perm.copy()
                    permCopy.insert(j, nums[ind])  
                    res.append(permCopy)
            return res
            
        return backtracking(0)