# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for node1,node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        visited = set()
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    if dfs(n, visited):
                        return True
            return False
        return dfs(source,visited)