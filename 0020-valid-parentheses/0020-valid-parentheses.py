class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesStack = []
        openParentheses = set(['(', '[', '{'])
        closedParentheses = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for st in s:
            if st in openParentheses:
                parenthesesStack.append(st)
            else:
                if st not in closedParentheses:
                    return False
                if len(parenthesesStack) == 0 or parenthesesStack[-1] !=  closedParentheses[st]:
                    return False
                parenthesesStack.pop()
        return len(parenthesesStack) == 0