class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxW = 0
        n = len(nums)
        numZeros = 0
        for r in range(n):
            if nums[r] == 0:
                numZeros += 1
            while numZeros > k:
                if nums[left] == 0:
                    numZeros-=1
                left += 1
            maxW = max(maxW,r-left+1)                    
        return maxW
                