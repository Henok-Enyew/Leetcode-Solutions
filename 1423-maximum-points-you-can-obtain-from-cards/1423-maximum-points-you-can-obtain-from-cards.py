class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        total = sum(cardPoints)
        window_size = len(cardPoints) - k
        current_window_sum = sum(cardPoints[:window_size])
        min_window_sum = current_window_sum
        for i in range(window_size, len(cardPoints)):
            current_window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, current_window_sum)
            
        return total - min_window_sum