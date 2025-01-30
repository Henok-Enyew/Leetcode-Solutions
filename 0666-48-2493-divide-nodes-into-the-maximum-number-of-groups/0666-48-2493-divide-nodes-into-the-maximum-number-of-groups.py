from collections import deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def bfs(start):
            q = deque([(start, 1)])
            level = {}
            level[start] = 1
            max_depth = 1
            while q:
                node, depth = q.popleft()
                for neighbor in graph[node]:
                    if neighbor in level:
                        if abs(level[neighbor] - depth) != 1:
                            return -1
                    else:
                        level[neighbor] = depth + 1
                        max_depth = max(max_depth, depth + 1)
                        q.append((neighbor, depth + 1))
            return max_depth

        graph = {i: [] for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        result = 0

        for i in range(1, n + 1):
            if i not in visited:
                component = set()
                q = deque([i])
                while q:
                    node = q.popleft()
                    if node in visited:
                        continue
                    visited.add(node)
                    component.add(node)
                    q.extend(graph[node])

                max_groups = -1
                for node in component:
                    max_groups = max(max_groups, bfs(node))
                    if max_groups == -1:
                        return -1
                result += max_groups

        return result
