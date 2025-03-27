from collections import Counter
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        dom = max(freq, key=freq.get)
        
        left_count = 0
        for i in range(n - 1):
            if nums[i] == dom:
                left_count += 1
            if left_count * 2 > (i + 1) and (freq[dom] - left_count) * 2 > (n - i - 1):
                return i
        return -1
