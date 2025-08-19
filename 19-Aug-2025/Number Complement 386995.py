# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)
        compl = ''
        for b in binary[2:]:
            if b == '0':
                compl += '1'
            else:
                compl += '0'
        return int(compl, 2)