class Solution:
    def repeatedCharacter(self, s: str) -> str:
        map = {}
        for i in range(len(s)):
            if s[i] in map.keys():
                map[s[i]] = 2
                return s[i]
            else:
                map[s[i]] = 1 

        