class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(1,len(s)):
            left_zeros = s[:i].count('0')
            right_ones = s[i:].count('1')

            max_score = max(max_score, left_zeros+right_ones)
        
        return max_score