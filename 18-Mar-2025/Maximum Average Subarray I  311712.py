# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_sum = sum(nums[:k])
        j = 0
        max_ave = win_sum / k
        for i in range(k,len(nums)):
            win_sum = win_sum - nums[j] + nums[i]
            j+=1
            max_ave = max(max_ave, win_sum/k)
        return max_ave