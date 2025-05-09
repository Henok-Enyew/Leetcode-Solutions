# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # return math.floor(-0.5 + math.sqrt((2*n) + 0.25))
        left, right = 0, n
        ans = float('-inf')
        while left <= right:
            mid = (left + right) // 2
            res = (mid + 1) * (mid) / 2
            if res <= n:
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans