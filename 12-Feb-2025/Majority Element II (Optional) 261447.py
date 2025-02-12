# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map = collections.Counter(nums)
        output  = []
        for key in map:
            if map[key]  > len(nums) / 3:
                output.append(key) 
        return output