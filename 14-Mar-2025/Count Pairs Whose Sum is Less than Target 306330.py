# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            sm = nums[left] + nums[right]
            
            if sm < target:
                count += (right - left)
                left += 1  
            else:
                right -= 1 
        return count
