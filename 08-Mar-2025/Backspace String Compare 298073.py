# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackT = []
        stackS =[]
        for ss in s:
            if len(stackS) and ss == '#':
                stackS.pop()
            elif ss != '#':
                stackS.append(ss)
        for tt in t:
            if len(stackT) and tt == '#':
                stackT.pop()
            elif tt != '#':
                stackT.append(tt)
        return stackT == stackS