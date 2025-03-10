# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0
        left, right  = 0 , len(height) -1
        while(left < right):
            area = (right - left) * min(height[left] , height[right])
            maxArea = max(maxArea , area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea