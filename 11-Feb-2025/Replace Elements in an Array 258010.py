# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = i
        for op in operations:
            index = mp[op[0]]
            nums[index] = op[1]
            mp[op[1]] = index
            del mp[op[0]]
        return nums