# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map = collections.Counter(nums)
        output  = []
        for key in map:
            if map[key]  > len(nums) / 3:
                output.append(key) 
        return output