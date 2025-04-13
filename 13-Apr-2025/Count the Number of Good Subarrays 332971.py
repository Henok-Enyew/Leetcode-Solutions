# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l = len(nums)

        counts = collections.Counter()
        left = 0
        pairs = 0
        ans = 0 
        for right in range(l):
            pairs += counts[nums[right]]
            counts[nums[right]] += 1

            while pairs >= k:
                counts[nums[left]] -= 1
                pairs -= counts[nums[left]]
                left += 1
            ans += left
        return ans