# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0

        for right in range(len(s)):
            last_seen[s[right]] = right

            if -1 not in last_seen.values():
                count += min(last_seen.values()) + 1

        return count
