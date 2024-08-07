class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i,v in enumerate(nums):
            if(v == 0):
                nums.remove(v)
                nums.append(0) 