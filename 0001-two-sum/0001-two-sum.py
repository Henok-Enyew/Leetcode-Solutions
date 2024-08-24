class Solution:
    def twoSum(self,nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_map:
                return [num_map[difference], i]
            num_map[num] = i
        return None
