# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for x, y in allowedSwaps:
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_y] = root_x

        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)

        res = 0
        for indices in components.values():
            source_counter = Counter([source[i] for i in indices])
            target_counter = Counter([target[i] for i in indices])
            res += sum((source_counter - target_counter).values())

        return res