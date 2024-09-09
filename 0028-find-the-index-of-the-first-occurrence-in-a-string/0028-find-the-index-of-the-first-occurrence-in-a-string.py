class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        c = 0
        j=0
        answer = -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                j=i
                k=0
                c=0
                while k<len(needle) and j<len(haystack) and haystack[j] == needle[k]:
                    k+=1
                    j+=1
                    c+=1
                if c == len(needle):
                    return i
        return -1

