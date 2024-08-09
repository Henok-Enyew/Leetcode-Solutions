class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        for st in s:
            if st == '#':
                if len(stackS) != 0:
                    stackS.pop()
            else: 
                stackS.append(st)
        for tt in t :
            if tt == '#':
                if len(stackT) != 0:
                    stackT.pop()
            else: 
                stackT.append(tt)
        return stackS == stackT