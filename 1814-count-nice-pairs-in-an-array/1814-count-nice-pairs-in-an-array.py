class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        res, d = 0, defaultdict(int)
        for i, n in enumerate(nums):
            k = n - int(str(n)[::-1])
            res += d[k]
            d[k] += 1
        return res % (10**9 + 7)