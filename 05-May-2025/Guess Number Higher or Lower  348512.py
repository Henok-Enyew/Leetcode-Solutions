# Problem: Guess Number Higher or Lower  - https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        res = None
        num = n
        up = n
        low = 0
        while res != 0:
            res = guess(num)
            if res == 0:
                break
            elif res == 1:
                low = num
                num = math.floor((low + up) / 2)
            elif res == -1:
                up = num
                num = math.floor((low + up) / 2) 
        return num