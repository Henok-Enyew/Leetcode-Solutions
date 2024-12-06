class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)  # Convert banned list to a set for faster lookup
        total_sum = 0
        count = 0
        
        for i in range(1, n + 1):
            if i not in banned_set and total_sum + i <= maxSum:
                total_sum += i
                count += 1
            elif total_sum + i > maxSum:
                break
        
        return count
