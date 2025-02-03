class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        answer = 1
        strictlyIncreasing = 1
        strictlyDecreasing = 1
        length=1
        isMono = False
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                length+=1
            else:
                length = 1
            strictlyIncreasing = max(strictlyIncreasing,length)
        length = 1
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                length+=1
            else:
                length = 1
            strictlyDecreasing = max(strictlyDecreasing,length)
            
        return max(strictlyIncreasing,strictlyDecreasing)