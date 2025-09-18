# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_factor_sum(x: int) -> int:
            total, num = 0, x
            factor = 2
            while factor * factor <= num:
                while num % factor == 0:
                    total += factor
                    num //= factor
                factor += 1
            if num > 1:
                total += num
            return total

        while True:
            s = prime_factor_sum(n)
            if s == n:
                return n
            n = s