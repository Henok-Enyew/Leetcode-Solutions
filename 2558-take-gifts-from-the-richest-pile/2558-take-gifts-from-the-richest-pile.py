import heapq
from math import isqrt

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            remaining = isqrt(largest)
            heapq.heappush(max_heap, -remaining)
        return -sum(max_heap)
