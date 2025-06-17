# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def backtracking(i, curComb):
            if len(curComb) == k:
                combinations.append(curComb[:])
                return 
            if i > n:
                return

            # take the number :)
            curComb.append(i)
            backtracking(i+1,curComb)
            curComb.pop()

            # leave the number :(
            backtracking(i+1, curComb)
        backtracking(1,[])
        return combinations