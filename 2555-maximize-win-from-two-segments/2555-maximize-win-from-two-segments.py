class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        maximal = 0
        n = len(prizePositions)

        dp = [0] * n 

        start = 0
        for end in range(n):
            while prizePositions[end] - prizePositions[start] > k:
                start += 1 
            
            segment_reward = end - start + 1
            dp[end] = max(dp[end-1], segment_reward)

            best_left = 0 if start == 0 else dp[start-1]
            maximal = max(maximal, best_left + segment_reward)
        
        return maximal