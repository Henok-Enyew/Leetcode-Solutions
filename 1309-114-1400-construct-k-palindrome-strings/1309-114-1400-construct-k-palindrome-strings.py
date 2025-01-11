from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False        
        char_count = Counter(s)        
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        return odd_count <= k
