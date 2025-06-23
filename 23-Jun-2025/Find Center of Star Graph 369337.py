# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        mp = defaultdict(list)
        st = set()
        for i in range(len(edges)):
            st.add(edges[i][1])
            st.add(edges[i][0])
            mp[edges[i][1]].append(edges[i][0])
            mp[edges[i][0]].append(edges[i][1])
        center = None
        for k in mp.keys():
            if len(mp[k]) == (len(st) -1):
                center = k
        return center