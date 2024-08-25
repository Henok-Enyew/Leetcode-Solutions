class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                continue
            if nums[left] != 0:
                left+=1
                continue
            nums[left] = nums[right]
            nums[right] = 0
            left+=1
        return nums                