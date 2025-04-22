# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for st in s:
            if stack and st.isdigit():
                stack.pop()
            elif not st.isdigit() :
                stack.append(st)

        return ''.join(stack)