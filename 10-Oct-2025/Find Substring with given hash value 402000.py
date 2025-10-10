# Problem: Find Substring with given hash value - https://leetcode.com/problems/find-substring-with-given-hash-value/description/

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        ords = [ord(l) - ord('a') + 1 for l in s]
        pows = [pow(power,i,modulo) for i in range(k)]
        n = len(s)           
        hash0 = sum(pows[i]*ords[n-k+i] for i in range(k)) % (modulo)
        res = ''     
        if hash0 == hashValue:
            res = s[n-k:]

        for i in range(n-2,k-2,-1):
            sa = ords[i+1]
            sb = ords[i-k+1]
            hash0 -= sa*pows[-1]
            hash0 *= power
            hash0 += sb*pows[0]
            hash0 = hash0 % modulo
            
            if hash0 == hashValue:
                res =  s[i-k+1:i+1]
        return res