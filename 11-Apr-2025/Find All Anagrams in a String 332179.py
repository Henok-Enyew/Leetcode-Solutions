# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])
        result = []
        if s_count == p_count:
            result.append(0)
        for i in range(len(p), len(s)):
            start_char = s[i - len(p)]
            new_char = s[i]
            s_count[start_char] -= 1
            if s_count[start_char] == 0:
                del s_count[start_char]
            s_count[new_char] += 1
            if s_count == p_count:
                result.append(i - len(p) + 1)
        return result