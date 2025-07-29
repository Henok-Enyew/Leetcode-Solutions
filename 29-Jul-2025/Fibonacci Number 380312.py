# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        memo = {0: 0, 1: 1} 
        def cal(k: int) -> int:
            if k in memo:
                return memo[k]
            result = cal(k - 1) + cal(k - 2)
            memo[k] = result
            return result
        return cal(n)