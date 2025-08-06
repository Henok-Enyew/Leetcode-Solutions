# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        maxp = 0
        for i in range(len(prices)):
            minp = min(minp, prices[i])
            profit = prices[i] - minp
            maxp = max(profit,maxp)
        return maxp