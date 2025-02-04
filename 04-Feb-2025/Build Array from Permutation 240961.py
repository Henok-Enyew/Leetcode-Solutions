# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = []
        for i,num in enumerate(nums):
            answer.append(nums[num])
        return answer