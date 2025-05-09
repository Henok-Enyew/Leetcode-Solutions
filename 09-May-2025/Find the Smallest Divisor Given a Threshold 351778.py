# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l,r = 1,max(nums)
        res = r
        while l<=r:
            mid = (l+r) // 2
            sm =0
            for n in nums:
                sm += math.ceil(n/mid)
            print(sm)
            if sm <= threshold:
                res = min(res,mid)
                r = mid-1
            else:
                l = mid+1
        return res
