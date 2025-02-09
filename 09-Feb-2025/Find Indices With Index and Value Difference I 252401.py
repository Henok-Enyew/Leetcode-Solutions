# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        answer = [-1,-1]
        left,right =0,indexDifference
        while left<len(nums) - indexDifference:
            if abs(nums[right] - nums[left]) >= valueDifference and right - left >= indexDifference:
                answer[0] = left
                answer[1] = right
                break
            if right + 1 == len(nums):
                right = left + indexDifference
                left+=1
                continue
            right+=1
                
        return answer