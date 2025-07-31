# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)
        
        dp = set()
        dp.add(0)
        
        for num in nums:
            next_dp = dp.copy()
            for curr_sum in dp:
                if curr_sum + num == target:
                    return True
                if curr_sum + num < target:
                    next_dp.add(curr_sum + num)
            dp = next_dp
        
        return target in dp