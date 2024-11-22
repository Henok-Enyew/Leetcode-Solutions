from typing import List
from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = defaultdict(int)

        for row in matrix:
            normalized = tuple(cell ^ row[0] for cell in row)
            pattern_count[normalized] += 1
        return max(pattern_count.values())
