from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}  # Map value -> index
        dp = {}  # Dictionary to store Fibonacci-like subsequences
        max_len = 0

        for k in range(len(arr)):
            for j in range(k):
                i = index.get(arr[k] - arr[j])  # Check if arr[k] - arr[j] exists in arr
                if i is not None and i < j:  # Ensure it's a valid subsequence
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    max_len = max(max_len, dp[(j, k)])

        return max_len if max_len >= 3 else 0  # Must be at least length 3
