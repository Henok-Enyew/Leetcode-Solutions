# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        mp_chars = Counter(chars)  
        count = 0

        for w in words:
            mp_w = Counter(w)  
            is_all_in_char = True

            for key in mp_w:  
                if key not in mp_chars or mp_w[key] > mp_chars[key]:
                    is_all_in_char = False
                    break

            if is_all_in_char:
                count += len(w) 

        return count