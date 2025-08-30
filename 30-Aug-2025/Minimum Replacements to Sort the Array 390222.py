# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        N = len(nums)
        prev_value = nums[-1]
        total_opt = 0


        for index in range(N - 2, -1, -1):
            new_value = nums[index]
            
            if new_value <= prev_value:
                prev_value = nums[index]
                continue
            curr_opt =ceil( new_value /prev_value) 
            prev_value = new_value // curr_opt
            total_opt += curr_opt - 1
        return total_opt
