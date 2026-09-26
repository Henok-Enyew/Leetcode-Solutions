class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            temp = n
            digits = ''
            while temp > 0:
                rem = temp % i
                digits = str(rem) + digits
                temp = temp // i
            if digits != digits[::-1]:
                return False
        return True