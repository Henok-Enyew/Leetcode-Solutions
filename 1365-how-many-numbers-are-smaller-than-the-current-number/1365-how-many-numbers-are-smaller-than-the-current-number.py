class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsSorted = sorted(nums)
        result = []
        for num in nums:
            result.append(numsSorted.index(num))
        return result