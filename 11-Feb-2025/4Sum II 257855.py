# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        mp = collections.Counter()
        for i in nums1:
            for j in nums2:
                mp[i+j] += 1
        answer = 0
        for i in nums3:
            for j in nums4:
                answer += mp[-(i+j)]
        return answer
        