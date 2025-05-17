# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        ans = float('-inf')
        while left <= right:
            mid = (left + right) // 2
            sm = (mid + 1) * (mid) / 2
            if sm <= n:
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans