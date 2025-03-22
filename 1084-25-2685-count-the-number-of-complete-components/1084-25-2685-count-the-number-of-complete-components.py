from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        complete_components = 0
        
        for i in range(n):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                
                is_complete = True
                m = len(component)
                for node in component:
                    if len(graph[node]) != m - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    complete_components += 1
        
        return complete_components