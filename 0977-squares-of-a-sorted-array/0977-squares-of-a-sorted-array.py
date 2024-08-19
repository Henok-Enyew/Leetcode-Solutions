class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            answer.append(num * num)
        return sorted(answer)