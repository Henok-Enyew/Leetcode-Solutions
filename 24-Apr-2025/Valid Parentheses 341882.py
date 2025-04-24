# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            '(':')',
            '{':'}',
            '[':']'
        }
        for st in s:
            if st in mp:
                stack.append(st)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if mp[last] != st:
                    return False    
                    
        return True if not stack else False