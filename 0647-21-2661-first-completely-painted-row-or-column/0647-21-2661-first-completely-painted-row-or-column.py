from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        pos = {mat[i][j]: (i, j) for i in range(m) for j in range(n)}
        row_count, col_count = [0] * m, [0] * n
        for i, num in enumerate(arr):
            r, c = pos[num]
            row_count[r] += 1
            col_count[c] += 1
            if row_count[r] == n or col_count[c] == m:
                return i
        return -1
