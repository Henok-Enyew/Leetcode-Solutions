# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return math.floor(-0.5 + math.sqrt((2*n) + 0.25))
