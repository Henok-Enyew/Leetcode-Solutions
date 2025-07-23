# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

from typing import List

class Solution:
    def dfs(self, i: int, adj: List[List[int]], hash: set, visited: List[bool], stack: List[int]) -> bool:
        hash.add(i)
        visited[i] = True

        for neighbor in adj[i]:
            if not visited[neighbor]:
                if not self.dfs(neighbor, adj, hash, visited, stack):
                    return False
            elif neighbor in hash:
                return False

        hash.remove(i)
        stack.append(i)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj[src].append(dest)

        visited = [False] * numCourses
        stack = []

        for i in range(numCourses):
            if not visited[i]:
                hash = set()
                if not self.dfs(i, adj, hash, visited, stack):
                    return []
##
        return stack[::-1] 