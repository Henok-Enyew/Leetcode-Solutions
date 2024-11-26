from typing import List
from collections import defaultdict, deque

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        champions = [node for node in range(n) if in_degree[node] == 0]
        
        if len(champions) != 1:
            return -1
        
        champion = champions[0]
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        
        dfs(champion)
        
        if len(visited) != n:
            return -1
        
        return champion
