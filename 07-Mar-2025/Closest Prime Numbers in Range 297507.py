# Problem: Closest Prime Numbers in Range - https://leetcode.com/problems/closest-prime-numbers-in-range/

from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return [i for i in range(max(2, left), n + 1) if is_prime[i]]

        primes = sieve(right)

        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        ans = [-1, -1]

        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < min_diff:
                min_diff = primes[i + 1] - primes[i]
                ans = [primes[i], primes[i + 1]]

        return ans
