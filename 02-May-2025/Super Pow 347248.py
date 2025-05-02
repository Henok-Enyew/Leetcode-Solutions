# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        bs = ''
        for bb in b:
            bs += str(bb)
        s = ''.join(bs)
        n = int(s)
        return pow(a,n, 1337)