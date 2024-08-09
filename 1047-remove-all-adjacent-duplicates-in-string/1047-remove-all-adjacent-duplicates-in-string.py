class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for st in s:
            if(len(stack) != 0 and stack[-1] == st):
                stack.pop()
            else:
                stack.append(st)
        return "".join(stack)