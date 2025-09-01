# Problem: Alian Dictionary - https://www.geeksforgeeks.org/problems/alien-dictionary/1

from collections import deque

class Solution:
    def findOrder( words):
     
        indeg = {c: set() for w in words for c in w}
        out = {c: set() for c in indeg}

        
        for a, b in zip(words, words[1:]):
            
            if len(a) > len(b) and a.startswith(b):
                return ""
            for ca, cb in zip(a, b):
                if ca != cb:
                    if cb not in out[ca]:          
                        out[ca].add(cb)
                        indeg[cb].add(ca)
                    break  

        
        q = deque([c for c, preds in indeg.items() if not preds])
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in list(out[u]):
                out[u].remove(v)
                indeg[v].remove(u)
                if not indeg[v]:
                    q.append(v)

        return "".join(order) if len(order) == len(indeg) else ""
