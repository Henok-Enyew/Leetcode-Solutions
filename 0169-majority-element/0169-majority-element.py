class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        map = {}
        for i,v in enumerate(nums):
            if v in map.keys():
                map[v] += 1
            else:
                map[v] = 1
        for k,v in map.items():
            if(v > len(nums) / 2):
                return k