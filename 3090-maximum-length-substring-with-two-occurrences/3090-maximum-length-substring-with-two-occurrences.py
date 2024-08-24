class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_length = 0
        frequency = {}
        left = 0

        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right], 0) + 1

            while frequency[s[right]] > 2:
                frequency[s[left]] -= 1

                # Delete leftmost char.
                if frequency[s[left]] == 0:
                    del frequency[s[left]]

                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length

