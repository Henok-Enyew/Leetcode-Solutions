class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        i = 0
        while i<len(nums):
            answer += nums[i]
            i+=2
        return answer