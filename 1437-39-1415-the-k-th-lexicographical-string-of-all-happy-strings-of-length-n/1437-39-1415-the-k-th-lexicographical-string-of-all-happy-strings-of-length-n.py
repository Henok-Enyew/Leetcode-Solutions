from itertools import product

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []
        
        def backtrack(path):
            if len(path) == n:
                happy_strings.append("".join(path))
                return
            for ch in "abc":
                if not path or path[-1] != ch:
                    backtrack(path + [ch])
        
        backtrack([])
        return happy_strings[k - 1] if k <= len(happy_strings) else ""
