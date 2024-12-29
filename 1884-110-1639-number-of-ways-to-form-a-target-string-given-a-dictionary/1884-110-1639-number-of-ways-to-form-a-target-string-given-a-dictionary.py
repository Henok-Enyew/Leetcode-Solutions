from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        word_len = len(words[0])
        target_len = len(target)
        
        char_count = [[0] * 26 for _ in range(word_len)]
        for word in words:
            for i, char in enumerate(word):
                char_count[i][ord(char) - ord('a')] += 1
        
        dp = [[0] * (word_len + 1) for _ in range(target_len + 1)]
        for j in range(word_len + 1):
            dp[0][j] = 1  # 1 way to form empty target
        
        for i in range(1, target_len + 1):
            for j in range(1, word_len + 1):
                dp[i][j] = dp[i][j-1]
                
                target_char = target[i-1]
                char_idx = ord(target_char) - ord('a')
                if char_count[j-1][char_idx] > 0:
                    dp[i][j] += dp[i-1][j-1] * char_count[j-1][char_idx]
                    dp[i][j] %= MOD
        
        return dp[target_len][word_len]
