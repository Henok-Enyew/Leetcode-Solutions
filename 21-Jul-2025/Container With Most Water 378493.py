# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0
        l, right  = 0 , len(height) -1
        while(l < right):
            area = (right - l) * min(height[l] , height[right])
            maxArea = max(maxArea , area)
            if height[l] < height[right]:
                l += 1
            else:
                right -= 1
        return maxArea