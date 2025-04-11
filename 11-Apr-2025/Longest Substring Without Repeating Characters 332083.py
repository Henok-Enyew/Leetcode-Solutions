# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        max_len = 0
        stt = 0
        for i,st in enumerate(s):
            if st in mp and mp[st] >= stt:
                stt = mp[st]+1
            mp[st] = i 
            max_len = max(max_len, i-stt+1)
        return max_len