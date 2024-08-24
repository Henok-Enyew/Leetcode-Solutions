class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            sum = nums[i] + nums[i+1]
            for j in range(i+1, len(nums)-1):
                if nums[j] + nums[j+1] == sum:
                    return True