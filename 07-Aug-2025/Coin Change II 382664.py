# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(len(coins) + 1)] for _ in range(amount + 1)]
        n = len(coins)

        for i in range(n + 1):
            dp[0][i] = 1

        for index in range(n):
            dp[0][index] = 1

        dp[0][n] = 1

        for target in range(1, amount + 1):
            for index in range(len(coins) - 1, -1, -1):
                if target < coins[index]:
                    dp[target][index] = dp[target][index + 1]
                else:
                    dp[target][index] = dp[target][index + 1] + dp[target - coins[index]][index]

        return dp[amount][0]
