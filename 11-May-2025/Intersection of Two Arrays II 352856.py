# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        for num in nums1:
            l,r = 0, len(nums2) -1 
            while l <= r:
                m = (l+r) // 2
                if num == nums2[m]:
                    ans.append(num)
                    nums2.pop(m)
                    break
                elif num > nums2[m]:
                    l = m+1
                elif num < nums2[m]:
                    r = m - 1
        return ans
