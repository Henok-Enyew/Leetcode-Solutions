# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        res = []
        nums.sort()
        def backtracking(ind, perm):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for i in range(0, len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i-1] == nums[i] and not visited[i-1]:
                    continue
                
                perm.append(nums[i])
                visited[i] = True
                backtracking(i+1, perm)
                visited[i] = False
                perm.pop()
        backtracking(0,[])
        return res