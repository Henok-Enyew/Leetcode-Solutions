# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime = set()
        def primeFactors(n):
            d = 2
            while d * d <= n:
                while n % d == 0:
                    prime.add(d)
                    n //= d
                d+=1
            if n > 1:
                prime.add(n)

        for num in nums:
            primeFactors(num)

        return len(prime)
        