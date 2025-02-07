from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_map = {}
        color_count = {}
        result = []

        for x, y in queries:
            if x in color_map:
                prev_color = color_map[x]
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    del color_count[prev_color]
            
            color_map[x] = y
            color_count[y] = color_count.get(y, 0) + 1
            result.append(len(color_count))

        return result
