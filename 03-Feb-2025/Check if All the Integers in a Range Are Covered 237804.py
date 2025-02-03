# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        map = {}
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                map[j] = 1
        for i in range(left, right+1):
            if i not in map:
                return False
        return True