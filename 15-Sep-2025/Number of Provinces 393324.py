# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                queue = deque([i])
                while queue:
                    node = queue.popleft()
                    visited[node] = True
                    for j in range(n):
                        if isConnected[node][j] and not visited[j]:
                            queue.append(j)
                count += 1
        return count