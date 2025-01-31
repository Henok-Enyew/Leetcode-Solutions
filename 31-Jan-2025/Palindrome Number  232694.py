# Problem: Palindrome Number  - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        strin = f"{x}"
        rev = ''
        for i in range(len(strin)-1,-1,-1):
            rev+=strin[i]
        return strin == rev