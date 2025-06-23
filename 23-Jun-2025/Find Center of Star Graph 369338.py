# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]