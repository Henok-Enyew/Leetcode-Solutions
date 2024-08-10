import math
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        rightSum = []
        result = []
        j = len(nums) - 1
        sumL = 0
        sumR = 0
        for num in nums:
            leftSum.append(sumL)
            rightSum.insert(0,sumR)
            sumL += num
            sumR += nums[j]
            j -= 1
        for i,sum in enumerate( leftSum):
            diff = math.fabs(sum - rightSum[i])
            result.append(int(diff))
        return result