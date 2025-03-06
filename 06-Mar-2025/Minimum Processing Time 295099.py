# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)

        max_time = 0
        i = 0
        j=0
        while i+4<=len(tasks):
            max_time  = max(max_time, max(tasks[i:i+4]) + processorTime[j])
            i+=4
            j+=1
        return max_time