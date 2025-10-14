# Problem: Number of Ways to Arrive at Destination - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

from heapq import heappop, heappush
from collections import defaultdict
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        heap = [(0, 0)]
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        while heap:
            d, node = heappop(heap)
            if d > dist[node]:
                continue

            for neighbor, time in graph[node]:
                new_dist = d + time
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    ways[neighbor] = ways[node]
                    heappush(heap, (new_dist, neighbor))
                elif new_dist == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1] % MOD