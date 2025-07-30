# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        memo = {1: 1, 2: 2} 
        def cal(k: int) -> int:
            if k in memo:
                return memo[k]
            memo[k]  = cal(k - 1) + cal(k - 2)
            return memo[k] 
        return cal(n)