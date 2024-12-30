class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (high + 1)
        dp[0] = 1  
        
        for length in range(1, high + 1):
            if length >= zero:
                dp[length] = (dp[length] + dp[length - zero]) % MOD
            if length >= one:
                dp[length] = (dp[length] + dp[length - one]) % MOD

        result = 0
        for length in range(low, high + 1):
            result = (result + dp[length]) % MOD
        
        return result
