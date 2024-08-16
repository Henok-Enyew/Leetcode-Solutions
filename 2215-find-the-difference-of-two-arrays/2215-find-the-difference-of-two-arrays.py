class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]
        num1Map = {}
        num2Map = {}
        for num1 in nums1:
            num1Map[num1] = 1
        for num2 in set(nums2):
            num2Map[num2] = 1
            if(num2 not in num1Map):
                answer[1].append(num2)
        for num1 in set(nums1):
            if num1 not in num2Map:
                answer[0].append(num1)
        return answer