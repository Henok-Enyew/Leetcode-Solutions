# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

from collections import defaultdict, deque
from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        #######initialize
        graph = defaultdict(list)
        in_degree = [0] * n

        for u, v in richer:
            graph[u].append(v)
            in_degree[v] += 1

        answer = [i for i in range(n)] 
        q = deque()

        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()

            for neighbor in graph[node]:
                if quiet[answer[node]] < quiet[answer[neighbor]]:
                    answer[neighbor] = answer[node] 

                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
                
        return answer