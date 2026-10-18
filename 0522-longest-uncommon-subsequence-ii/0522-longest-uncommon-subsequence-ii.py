class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        d=defaultdict(lambda:0)
        def trv(word,i,curr=''):
            if i==len(word):
                if curr:    d[curr]+=1
                return 
            trv(word,i+1,curr+word[i])
            trv(word,i+1,curr)
        for w in strs:
            trv(w,0,'')
        return max([len(w) for w,f in d.items() if f==1],default=-1)