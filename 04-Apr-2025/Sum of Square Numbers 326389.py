# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = {}
        i = 0
        while i**2 <= c:
            squares[i**2] = i
            if c - i**2 in squares:
                return True
            i+=1
        return False