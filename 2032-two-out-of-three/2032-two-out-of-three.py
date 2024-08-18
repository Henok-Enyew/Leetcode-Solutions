class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        map1 = {}
        map2 = {}
        answer = []
        for num1 in nums1:
            map1[num1] = 1
        for num2 in nums2:
            if num2 in map1:
                answer.append(num2)
            map2[num2] = 1
        for num3 in nums3:
            if num3 in map1 or num3 in map2:
                answer.append(num3)
        return set(answer)