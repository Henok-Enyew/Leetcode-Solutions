class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inters = []
        nums1Map = {}
        for num1 in nums1:
            nums1Map[num1] = 1
        for num2 in set(nums2):
            if num2 in nums1Map:
                inters.append(num2)
        return inters
