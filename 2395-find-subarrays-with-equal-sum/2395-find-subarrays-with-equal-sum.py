class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        map  = {}
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] in map:
                return True
            map[nums[i] + nums[i+1]] = 1