class Solution:
    def repeatedCharacter(self, s: str) -> str:
        store = []
        for st in s:
            if(st in store):
                return st
            else:
                store.append(st)
       

        