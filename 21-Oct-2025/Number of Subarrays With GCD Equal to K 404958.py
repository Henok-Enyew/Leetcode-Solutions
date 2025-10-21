# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, a: List[int], k: int) -> int:
        return sum(gcd(*a[i:j+1])==k for i,j in product(*[range(len(a))]*2))