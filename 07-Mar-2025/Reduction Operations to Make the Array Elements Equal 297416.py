# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        largest = nums[0] 
        i=1
        count = 1
        if nums[0] == nums[len(nums)-1]:
            return 0
        while i<len(nums)-1 and nums[i] != nums[len(nums)-1]:
            if nums[i] == largest:
                count += 1
            else:
                count = count + i+1
                largest = nums[i]
            i+=1 
        return count
