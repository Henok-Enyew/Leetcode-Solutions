class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        map = {}
        counter = 0
        for i,num in enumerate( nums):
            map[num] = i
        for key,value in map.items():
            if(key - diff in map.keys() and key - 2 * diff in map.keys()):
                counter += 1
        return counter