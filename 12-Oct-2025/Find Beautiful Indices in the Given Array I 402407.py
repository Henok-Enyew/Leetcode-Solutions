# Problem: Find Beautiful Indices in the Given Array I - https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description/

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        f1=[]
        i=0
        j=0
        while(i<len(s)):
            aa=i
            while(j<len(a) and aa<len(s) and s[aa]==a[j]):
                j+=1
                aa+=1
            if(j==len(a)):
                f1.append(i)
            j=0
            i+=1
        i=0
        j=0
        f2=[]
        while(i<len(s)):
            aa=i
            while(j<len(b) and aa<len(s) and s[aa]==b[j]):
                j+=1
                aa+=1
            if(j==len(b)):
                f2.append(i)
            j=0
            i+=1
        ans=[]

        for i in f1:
            b1=bisect.bisect_right(f2,i+k)
            b2=bisect.bisect_left(f2,i-k)
            if(b1!=b2):
                ans.append(i)
        return ans
        