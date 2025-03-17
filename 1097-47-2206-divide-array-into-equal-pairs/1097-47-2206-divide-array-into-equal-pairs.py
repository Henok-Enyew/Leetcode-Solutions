class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0
        while i<len(nums)-1:
            if nums[i] != nums[i+1]:
                return False
            i+=2
        return True