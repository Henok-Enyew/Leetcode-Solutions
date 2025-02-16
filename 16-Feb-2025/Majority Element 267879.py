# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        mp = collections.Counter(nums)
        for key in mp:
            if mp[key] > len(nums) / 2:
                return key
