class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_length = 0
        frequency = {}
        left = 0
        for i,right in enumerate(s):
            if right not in frequency:
                frequency[right] = 1
            elif right in frequency:
                frequency[right] += 1
            while frequency[right] >2:
                frequency[s[left]] -= 1
                
                if frequency[s[left]] == 0:
                    del frequency[s[left]]
                left+=1
            max_length = max(max_length, i-left+1)
        return max_length
                