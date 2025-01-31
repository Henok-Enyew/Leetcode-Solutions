# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = []
        for st in s:
            if st.isalpha() or st.isdigit():
                answer.append(st.lower())
        return answer == answer[::-1]