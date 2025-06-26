# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        #
        for i in range(len(edges)):
            mp[edges[i][1]].append(edges[i][0])
        ans = []
        for i in range(n):
            if i not in mp.keys():
                ans.append(i)
        return ans