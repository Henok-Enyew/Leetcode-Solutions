import math
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        map = {}
        result = 0
        for x in nums:
            if x in map.keys():
                map[x] += 1
            else:
                map[x] = 1
        for key,value in map.items():
            result += math.floor(value*(value-1)/2)
        return result