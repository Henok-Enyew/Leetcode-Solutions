class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inters = []
        nums1Map = {}
        for num1 in nums1:
            if num1 not in nums1Map: 
                nums1Map[num1] = 1
            else:
                nums1Map[num1] += 1
        for num2 in nums2:
            if num2 in nums1Map and nums1Map[num2] >=1 :
                nums1Map[num2] -= 1
                inters.append(num2)
        return inters
