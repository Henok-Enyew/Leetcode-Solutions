# Problem: Minimum One Bit Operations to Make Integers Zero - https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n:
            res = -res - (n ^ (n - 1))
            n &= n - 1
        return abs(res)