# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        l = len(nums)
        left,right = 0,1
        print(nums)
        while left < l-1:
            sm = nums[left] + nums[right]
            while sm<target:
                count+=1
                print(left,right)
                if right + 1 < l:
                    right+=1
                else:
                    break
                sm = nums[left] + nums[right]
            left += 1
            right = left+1
        return count