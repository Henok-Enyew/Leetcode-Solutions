# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path_arr = path.split('/')
        stack = []
        for p in path_arr:
            if p == '.' or p == '':
                continue
            elif p == '..' and stack:
                stack.pop()
            elif p == '..':
                continue
            else:
                stack.append(f"{p}/")
        if stack:
            return '/'+''.join(stack)[:-1]
        else:
            return '/'
