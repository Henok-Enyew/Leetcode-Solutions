# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.dict = {}

    def addWord(self, word: str) -> None:
        t = self.dict
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['-'] = True

    def search(self, word: str) -> bool:
        t = self.dict
        n = len(word)
        def dfs(node, i):
            if i == n:
                return '-' in node
            c = word[i]
            if c == '.':
                for key, value in node.items():
                    if key == '-':
                        continue
                    else:
                        if dfs(value, i+1):
                            return True
                return False
            else:
                if c not in node:
                    return False
                return dfs(node[c], i+1)
        return dfs(t, 0)