class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or s == '' or t=='':
            return False
        sl = list(s)
        tl = list(t)
        sl.sort()
        tl.sort()
        return ''.join(sl) == ''.join(tl)