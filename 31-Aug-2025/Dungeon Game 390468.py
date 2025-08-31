# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0]*n for i in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[i][j] = max(1, 1-dungeon[i][j])
                else:
                    if i == m-1:
                        dp[i][j] = max(1, dp[i][j+1] - dungeon[i][j])
                    elif j == n-1:
                        dp[i][j] = max(1, dp[i+1][j] - dungeon[i][j])
                    else:
                        bottom = max(1, dp[i+1][j] - dungeon[i][j])
                        right = max(1, dp[i][j+1] - dungeon[i][j])
                        dp[i][j] = min(bottom, right)
        
        return dp[0][0]