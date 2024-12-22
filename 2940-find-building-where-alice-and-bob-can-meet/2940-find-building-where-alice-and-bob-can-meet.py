class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [float('inf')] * (size + 1)

    def update(self, index: int, value: int):
        while index <= self.size:
            self.tree[index] = min(self.tree[index], value)
            index += index & -index

    def query(self, index: int) -> int:
        minimum = float('inf')
        while index > 0:
            minimum = min(minimum, self.tree[index])
            index -= index & -index
        return -1 if minimum == float('inf') else minimum


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        num_buildings, num_queries = len(heights), len(queries)

        normalized_queries = [[min(query), max(query)] for query in queries]

        sorted_heights = sorted(set(heights))
        results = [-1] * num_queries
        fenwick = FenwickTree(num_buildings)
        current_index = num_buildings - 1

        for query_index in sorted(range(num_queries), key=lambda x: -normalized_queries[x][1]):
            left, right = normalized_queries[query_index]

            while current_index > right:
                tree_index = num_buildings - bisect_left(sorted_heights, heights[current_index]) + 1
                fenwick.update(tree_index, current_index)
                current_index -= 1

            if left == right or heights[left] < heights[right]:
                results[query_index] = right
            else:
                tree_index = num_buildings - bisect_left(sorted_heights, heights[left])
                results[query_index] = fenwick.query(tree_index)

        return results
