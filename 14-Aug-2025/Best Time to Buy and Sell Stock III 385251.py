# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [[[-1 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]

        def dfs(day, trans, buy):
            # base case
            if day >= len(prices):
                return 0
            if trans == 0:
                return 0
            
            if dp[day][trans][buy] != -1:
                return dp[day][trans][buy]

            if buy:
                sell = prices[day] + dfs(day + 1, trans - 1, 0)
                not_sell = dfs(day + 1, trans, 1)
                dp[day][trans][buy] = max(sell, not_sell)
                return dp[day][trans][buy]
            else:
                buy_ = -prices[day] + dfs(day + 1, trans, 1)
                not_buy = dfs(day + 1, trans, 0)
                dp[day][trans][buy] = max(buy_, not_buy)
                return dp[day][trans][buy]

        return dfs(0, 2, 0)