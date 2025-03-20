# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        max_global = 0
        memo = k
        for i in range(26):
            cur_char = chr(65+i)
            left = 0 
            k = memo
            max_local = 0
            for right in range(N):
                while left <= right and k < 0:
                    if s[left] != cur_char:
                        k += 1
                    left += 1
                if s[right] != cur_char:
                    k -= 1
                if k >= 0:
                    max_local = max(max_local, right - left + 1)
            max_global = max(max_global, max_local)
        return max_global