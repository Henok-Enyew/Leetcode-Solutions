# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

from typing import List
from collections import Counter

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        points1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        points2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        vector_count = Counter()
        
        for r1, c1 in points1:
            for r2, c2 in points2:
                vector = (r2 - r1, c2 - c1)
                vector_count[vector] += 1

        return max(vector_count.values(), default=0)
