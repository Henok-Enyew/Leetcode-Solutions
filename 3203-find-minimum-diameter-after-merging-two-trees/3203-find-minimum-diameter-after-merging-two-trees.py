from collections import defaultdict
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edgeList1: List[List[int]], edgeList2: List[List[int]]) -> int:
        diameter1 = self.getTreeDiameter(edgeList1)
        diameter2 = self.getTreeDiameter(edgeList2)
        return max(diameter1, diameter2, (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1)

    def getTreeDiameter(self, edges: List[List[int]]) -> int:
        def depthFirstSearch(node: int, parent: int, depth: int):
            for neighbor in graph[node]:
                if neighbor != parent:
                    depthFirstSearch(neighbor, node, depth + 1)
            nonlocal maxDist, farthestNode
            if depth > maxDist:
                maxDist = depth
                farthestNode = node

        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        maxDist = farthestNode = 0
        depthFirstSearch(0, -1, 0)
        depthFirstSearch(farthestNode, -1, 0)
        return maxDist
