class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bits = bin(num2).count('1')
        result = 0
        for i in range(31, -1, -1):
            if set_bits > 0 and (num1 & (1 << i)):
                result |= (1 << i)
                set_bits -= 1
        for i in range(32):
            if set_bits > 0 and not (result & (1 << i)):
                result |= (1 << i)
                set_bits -= 1
        return result
