# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

from collections import defaultdict
from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = {}

        def dfs(node, c):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(neigh, 1 - c) for neigh in graph[node])
        
        return all(dfs(node, 0) if node not in color else True for node in range(1, n + 1))
