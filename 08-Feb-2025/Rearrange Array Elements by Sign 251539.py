# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postives = []
        negatives = []
        answer = []
        for i in range(len(nums)):
            if nums[i] > 0:
                postives.append(nums[i])
            else:
                negatives.append(nums[i])
        for i in range(int(len(nums)/2)):
            answer.append(postives[i])
            answer.append(negatives[i])
        return answer
        
