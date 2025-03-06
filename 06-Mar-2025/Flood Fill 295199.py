# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n, original = len(image), len(image[0]), image[sr][sc]
        if original == color:
            return image

        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and image[r][c] == original:
                image[r][c] = color
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        dfs(sr, sc)
        return image
