# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n + 1)]

        for day in range(n - 1, -1, -1):
            for trans in range(1, 3):
                sell = prices[day] + dp[day + 1][trans - 1][0]
                not_sell = dp[day + 1][trans][1]
                dp[day][trans][1] = max(sell, not_sell)

                buy_ = -prices[day] + dp[day + 1][trans][1]
                not_buy = dp[day + 1][trans][0]
                dp[day][trans][0] = max(buy_, not_buy)
        
        return dp[0][2][0]