from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        for pre, course in prerequisites:
            reachable[pre][course] = True
        
        for k in range(numCourses):  
            for i in range(numCourses):
                for j in range(numCourses):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
        result = []
        for u, v in queries:
            result.append(reachable[u][v])        
        return result
