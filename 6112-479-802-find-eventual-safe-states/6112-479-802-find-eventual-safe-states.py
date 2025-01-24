from typing import List
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        in_degree = [0] * n
        
        for node in range(n):
            for neighbor in graph[node]:
                reverse_graph[neighbor].append(node)
                in_degree[node] += 1
        
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        safe_nodes = []
        
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return sorted(safe_nodes)
