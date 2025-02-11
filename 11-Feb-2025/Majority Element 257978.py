# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        map = collections.Counter(nums)
        for key in map:
            if map[key] > len(nums) / 2:
                return key
