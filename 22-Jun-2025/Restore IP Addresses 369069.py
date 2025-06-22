# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(i, dots, cur):
            if dots == 4 and i == len(s):
                res.append(cur[:-1])
                return
            if dots >= 4:
                return
            for j in range(i, min(i+3, len(s))):
                num = int(s[i:j+1])
                if num <= 255 and (i == j or s[i] != '0'):
                    backtrack(j+1, dots+1, cur + s[i:j+1] + '.')
        
        backtrack(0,0,'')
        return res
