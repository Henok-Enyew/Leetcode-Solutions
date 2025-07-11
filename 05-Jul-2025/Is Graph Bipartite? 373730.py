# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node: int, c: int) -> bool:
            color[node] = c
            for nei in graph[node]:
                if color[nei] == -1:
                    if not dfs(nei, 1 - c):
                        return False
                elif color[nei] == color[node]:
                    return False
            return True
        
        for j in range(n):
            if color[j] == -1:
                if not dfs(j, 0):
                    return False
        return True