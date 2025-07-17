# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        ans = 0
        l =  sorted(costs, key=lambda x:(x[0]-x[1])) # Sorting happens Here
        for i in range(n):
            if i >= n//2:
                ans += l[i][1]
            else:
                ans += l[i][0]

        return ans