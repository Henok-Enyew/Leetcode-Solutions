# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        l = len(piles) / 3
        ans=0
        i = 1
        while l:
            ans += piles[i]
            i+=2
            l-=1
        return ans