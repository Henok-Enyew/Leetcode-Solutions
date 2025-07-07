# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for src, dest in redEdges:
            red[src].append(dest)
        for src, dest in blueEdges:
            blue[src].append(dest)
         
        q = deque()
        answer = [-1 for i in range(n)]
        q.append([0,0,None]) # node, length, prev_edge_color
        visited = set()
        visited.add((0,None))
        while q:
            cur, length, edgeColor = q.popleft()
            if answer[cur] == -1:
                answer[cur] = length
            if edgeColor != 'RED':
                for neibor in red[cur]:
                    if (neibor, "RED") not in visited:
                        q.append([neibor, length + 1, "RED"])
                        visited.add((neibor, "RED"))
            if edgeColor != 'BLUE':
                for neibor in blue[cur]:
                    if (neibor, "BLUE") not in visited:
                        q.append([neibor, length + 1, "BLUE"])
                        visited.add((neibor, "BLUE"))
        return answer
                        