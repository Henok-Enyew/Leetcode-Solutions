# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

from sortedcontainers import SortedDict
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sd = SortedDict()
        
        for index, (start, _) in enumerate(intervals):
            sd[start] = index
        
        ans = []
        for _, end in intervals:
            index = sd.bisect_left(end)
            if index < len(sd):
                ans.append(sd.values()[index])
            else:
                ans.append(-1)
        
        return ans
