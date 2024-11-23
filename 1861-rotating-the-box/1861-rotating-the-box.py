from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            empty = len(row) - 1  
            for col in range(len(row) - 1, -1, -1):
                if row[col] == '#':
                    row[col], row[empty] = row[empty], row[col]
                    empty -= 1
                elif row[col] == '*':  
                    empty = col - 1
        m, n = len(box), len(box[0])
        rotated_box = [[''] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated_box[j][m - i - 1] = box[i][j]
        return rotated_box
