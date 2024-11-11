class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        if(len(s) != len(t)):
            return False
        for i in range(len(s)):
            if s[i] in map.keys():
                if map[s[i]] != t[i]:
                    return False
            elif t[i] in map.values():
                    return False
            map[s[i]] = t[i]
        return True