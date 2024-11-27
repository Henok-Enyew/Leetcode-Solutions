from typing import List, Tuple
import heapq
from collections import defaultdict

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Step 1: Initialize graph with initial roads
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append((i + 1, 1))  # Road from i to i+1 with weight 1

        # Step 2: Function to find shortest path using Dijkstra's algorithm
        def dijkstra():
            dist = [float('inf')] * n
            dist[0] = 0
            min_heap = [(0, 0)]  # (distance, node)
            
            while min_heap:
                curr_dist, node = heapq.heappop(min_heap)
                
                # Skip if we already found a better path
                if curr_dist > dist[node]:
                    continue
                
                for neighbor, weight in graph[node]:
                    new_dist = curr_dist + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heapq.heappush(min_heap, (new_dist, neighbor))
            
            return dist[n - 1]

        # Step 3: Process each query and compute shortest path
        answer = []
        for u, v in queries:
            graph[u].append((v, 1))  # Add new road with weight 1
            shortest_path = dijkstra()
            answer.append(shortest_path if shortest_path != float('inf') else -1)

        return answer
