# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(o, c):
            if c == o == n:
                res.append("".join(stack))
                return
            if o < n:
                stack.append('(')
                backtrack(o+1,c)
                stack.pop()

            if c < o:
                stack.append(')')
                backtrack(o,c+1)
                stack.pop()
        backtrack(0,0)
        return res