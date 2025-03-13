# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = len(nums)
        left,right = 0,l-1
        count = 0
        while left<right:
            if nums[left] + nums[right]  == k:
                count+=1
                left+=1
                right-=1
            elif nums[left] + nums[right]  < k:
                left+=1
            elif nums[left] + nums[right]  > k:
                right-=1
        return count