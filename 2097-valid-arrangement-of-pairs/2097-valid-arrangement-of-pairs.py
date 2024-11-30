from collections import defaultdict, deque
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Step 1: Build the graph and track in-degrees and out-degrees
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        # Step 2: Find the starting point
        start_node = pairs[0][0]  # Default start node
        for node in graph:
            if out_degree[node] > in_degree[node]:
                start_node = node
                break
        
        # Step 3: Hierholzer's algorithm to find the Eulerian path
        stack = [start_node]
        result = []
        
        while stack:
            node = stack[-1]
            if graph[node]:
                next_node = graph[node].popleft()  # Remove the edge
                stack.append(next_node)
            else:
                result.append(stack.pop())
        
        # Step 4: Reverse the result to get the correct order
        result.reverse()
        
        # Convert the result into pairs
        return [[result[i], result[i + 1]] for i in range(len(result) - 1)]
