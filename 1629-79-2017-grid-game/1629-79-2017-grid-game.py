class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix_top = [0] * (n + 1)
        prefix_bottom = [0] * (n + 1)

        for i in range(n):
            prefix_top[i + 1] = prefix_top[i] + grid[0][i]
            prefix_bottom[i + 1] = prefix_bottom[i] + grid[1][i]

        result = float('inf')
        for i in range(n):
            top = prefix_top[n] - prefix_top[i + 1]
            bottom = prefix_bottom[i]
            result = min(result, max(top, bottom))

        return result
