# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return True
        j = nums[0]
        for i in range(l-1):
            if nums[i] + i >= l - 1:
                return True
            if nums[i] == 0 and j <= 1: 
                return False
            if nums[i] == 0:
                j -= 1
            else:
                j -= 1
                j =  max(j,nums[i])
            
        return False