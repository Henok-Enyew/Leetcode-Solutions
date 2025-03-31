from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0  # Only one group, so no difference in scores.

        pair_sums = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        
        pair_sums.sort()

        max_score = sum(pair_sums[-(k-1):])  # Sum of k-1 largest
        min_score = sum(pair_sums[:(k-1)])  # Sum of k-1 smallest

        return max_score - min_score
