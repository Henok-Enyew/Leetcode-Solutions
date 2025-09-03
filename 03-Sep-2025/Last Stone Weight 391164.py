# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]  
        heapq.heapify(stones) 
        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first != second:
                heapq.heappush(stones, -abs(first - second))
        if stones:
            return -stones[0]
        return 0