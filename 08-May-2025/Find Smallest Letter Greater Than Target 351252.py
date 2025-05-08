# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters) - 1

        while low <= high:
            mid = (low + high) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1

        return letters[low % len(letters)]
