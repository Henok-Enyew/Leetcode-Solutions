class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        l = len(s)
        longString = ""
        def isNiceString(start,end):
            st = set(s[start:end])
            for sg in st:
                if (sg.lower() in st) != (sg.upper() in st):
                    return False
            return True
        for start in range(l):
            for end in range(start + 1, l+1):
                if isNiceString(start,end) and end -start > len(longString):
                    longString = s[start: end]
        return longString
