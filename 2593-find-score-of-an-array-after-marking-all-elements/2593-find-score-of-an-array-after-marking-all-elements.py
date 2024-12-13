class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        indexed_nums = sorted((val, idx) for idx, val in enumerate(nums))
        score = 0

        for val, idx in indexed_nums:
            if not marked[idx]:
                score += val
                marked[idx] = True
                if idx > 0:
                    marked[idx - 1] = True
                if idx < n - 1:
                    marked[idx + 1] = True

        return score
