# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opr = set(['+', '-', '*', '/'])
        ##
        for t in tokens:
            if t in opr:
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if t == '+':
                    stack.append(op1 + op2)
                elif t == '-':
                    stack.append(op2 - op1)
                elif t == '*':
                    stack.append(op1 * op2)
                elif t == '/':
                    stack.append(int(op2 / op1))
                
            else:
                stack.append(t)
        return int(stack[0])