class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        maxAve = s / k
        left = 0
        for right in range(k,len(nums)):
            s -= nums[left]
            s += nums[right]
            maxAve = max(maxAve, s/k)
            left+=1
        return maxAve
            