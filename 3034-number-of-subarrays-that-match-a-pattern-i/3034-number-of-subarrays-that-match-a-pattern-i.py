
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:

        n, p, ans = len(nums), len(pattern), 0
        
        f = lambda x: (x[1] > x[0]) - (x[1] < x[0])

        arr = list(map(f, pairwise(nums)))

        return sum(arr[i:i+p] == pattern for i in range(n - p + 1))