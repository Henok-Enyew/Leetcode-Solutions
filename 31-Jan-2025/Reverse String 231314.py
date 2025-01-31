# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left,right = 0, len(s)-1
        while left<right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left+=1
            right-=1