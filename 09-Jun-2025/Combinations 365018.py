# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(first_num, path):
            if len(path) == k:
                ans.append(path[:])
                return

            for i in range(first_num, n + 1):
                path.append(i)
                backtracking(i+1, path)
                path.pop()
        
        ans = []
        backtracking(1,[])
        return ans