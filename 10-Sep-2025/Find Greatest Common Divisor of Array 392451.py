# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = max(nums), min(nums)
        while a > 0 and b > 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return b if a == 0 else a