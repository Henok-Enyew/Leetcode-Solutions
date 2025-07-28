# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        res = 0
        for start,finish in intervals[1:]:
            if start < end:
                res +=1
            else:
                end = finish
        return res