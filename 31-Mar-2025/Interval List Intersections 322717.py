# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        for f in firstList:
            for s in secondList:
                if f[1] >= s[0] and s[1] >= f[0]:
                    lower = max(f[0], s[0])
                    upper = min(f[1], s[1])
                    answer.append([lower,upper])
        return answer