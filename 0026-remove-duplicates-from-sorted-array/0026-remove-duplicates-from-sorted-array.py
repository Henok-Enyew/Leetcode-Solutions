class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        map = {}
        i=0
        j=0
        while i < len(nums):
            if nums[i] not in map:
                nums[j] = nums[i]
                map[nums[i]] = 1
                i += 1
                j += 1
            else:
                i+=1
        return j 