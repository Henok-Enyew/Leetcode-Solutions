# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left or num<=-self.left[0]:
            heapq.heappush(self.left,-num)
        else:
            heapq.heappush(self.right,num)
        
        if abs(len(self.left)-len(self.right))>1:
            if len(self.left)>len(self.right):
                elem = -heapq.heappop(self.left)
                heapq.heappush(self.right,elem)
            else:
                elem = heapq.heappop(self.right)
                heapq.heappush(self.left,-elem)

    def findMedian(self) -> float:
        if len(self.right)==len(self.left):
            return (-self.left[0]+self.right[0])/2
        elif len(self.left)>len(self.right):
            return -self.left[0]
        else:
            return self.right[0]

