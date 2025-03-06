class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def pickFirst(val):
            return val[0]
        i = 0
        answer = []
        intervals.sort(key=pickFirst)
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            i += 1
            while i < len(intervals) and end >= intervals[i][0] :           
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
                i+=1
            answer.append([start, end])
        return answer