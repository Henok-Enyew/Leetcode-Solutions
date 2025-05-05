# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def score(start: int, end: int) -> int:
            if start == end:
                return nums[start]
            pick_start = nums[start] - score(start + 1, end)
            pick_end = nums[end] - score(start, end - 1)
            return max(pick_start, pick_end)

        return score(0, len(nums) - 1) >= 0
