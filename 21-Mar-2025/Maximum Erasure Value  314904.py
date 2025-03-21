# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window_sum  = 0
        answer = 0
        N = len(nums)
        seen = set()
        left =0
        for right in range(N):
            while nums[right] in seen:
                seen.remove(nums[left])
                window_sum -= nums[left]
                left+=1
            seen.add(nums[right])
            window_sum += nums[right]
            answer = max(answer, window_sum)
        return answer