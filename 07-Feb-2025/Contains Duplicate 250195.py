# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2 = list(set(nums))
        return len(nums) != len(nums2) 