# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(st:str):
            return st == st[::-1]
        longest = ''
        l = len(s)
        for i in range(l):
            for j in range(i,l):
                if is_palindrome(s[i:j+1]):
                    longest = s[i:j+1] if len(longest) < j+1 - i + 1 else longest
        return longest