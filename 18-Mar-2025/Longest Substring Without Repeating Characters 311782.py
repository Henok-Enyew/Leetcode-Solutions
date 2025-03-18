# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        max_len = 0
        start = 0
        for i,st in enumerate(s):
            if st in mp and mp[st] >= start:
                start = mp[st]+1
            mp[st] = i 
            max_len = max(max_len, i-start+1)
        return max_len