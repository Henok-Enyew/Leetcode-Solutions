# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                st = ''
                while stack[-1] != '[':
                    pop = stack.pop()
                    st = pop + st
                stack.pop()
                nm = ''
                while stack and  stack[-1].isdigit(): 
                    pop = stack.pop()
                    nm = pop + nm
                nm = int(nm)
                for _ in range(nm):
                    stack.append(st)
            else:
                stack.append(s[i])

        return ''.join(stack)
        