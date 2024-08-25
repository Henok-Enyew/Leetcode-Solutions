class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        maxOnes = 0
        for num in nums:
            if num != 1:
                ones = 0
            else:
                ones += 1
                maxOnes = max(ones,maxOnes)
        return maxOnes