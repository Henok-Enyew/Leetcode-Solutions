from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total = Counter(s)
        if total['a'] < k or total['b'] < k or total['c'] < k:
            return -1
        required = {char: total[char] - k for char in 'abc'}
        n = len(s)
        left = 0
        max_length = 0
        window_count = Counter()
        for right in range(n):
            window_count[s[right]] += 1
            while (window_count['a'] > required['a'] or
                   window_count['b'] > required['b'] or
                   window_count['c'] > required['c']):
                window_count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return n - max_length
