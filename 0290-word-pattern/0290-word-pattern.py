class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns_map = {}
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            p = pattern[i]
            if p not in patterns_map.keys():
                if s[i] in patterns_map.values():
                    return False
                patterns_map[p] = s[i]
            elif patterns_map[p] != s[i]:
                return False
                
        return True
        