# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

from collections import deque, defaultdict
class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        def topo(adj,deg,sz):
            queue = deque(i for i in range(sz) if deg[i] == 0)
            out = []
            while queue:
                x = queue.popleft()
                out.append(x)
                for y in adj[x]:
                    deg[y] -= 1
                    if deg[y] == 0:
                        queue.append(y)
            return out if len(out) == sz else []
        
        cntGroups = m
        for i in range(n):
            if group[i] == -1:
                group[i] = cntGroups
                cntGroups += 1
        groupGraph, itemGraph = [set() for _ in range(cntGroups)],[set() for _ in range(n)]
        degG, degI = [0]*cntGroups, [0]*n
        for v in range(n):
            gv = group[v]
            for u in beforeItems[v]:
                if u == v:
                    return []
                gu = group[u]
                if u not in itemGraph[v]:
                    itemGraph[u].add(v)
                    degI[v] += 1
                if gu != gv and gv not in groupGraph[gu]:
                    groupGraph[gu].add(gv)
                    degG[gv] += 1
        
        groupsOrder = topo(groupGraph,degG[:],cntGroups)
        if not groupsOrder:
            return []
        itemsOrder = topo(itemGraph,degI[:],n)
        if not itemsOrder:
            return []
        topoOrder = defaultdict(list)
        for x in itemsOrder:
            topoOrder[group[x]].append(x)
        ans = []
        for g in groupsOrder:
            ans += topoOrder[g]
        return ans