class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = pow(10,9) + 7
        sum = 0
        l = len(nums)
        counts = [0] * l
        for start,end in requests:
            ende = end + 1
            counts[start] += 1
            if ende < l:
                counts[ende] -= 1
        for i in range(1, l):
            counts[i] += counts[i-1]
        nums.sort()
        counts.sort()
        for i in range(l):
            sum += (nums[i]) * counts[i]
        return sum % MOD