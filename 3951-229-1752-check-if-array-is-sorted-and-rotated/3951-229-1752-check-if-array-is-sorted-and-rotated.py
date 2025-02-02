
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = sum(nums[i] > nums[(i + 1) % len(nums)] for i in range(len(nums)))
        return count <= 1






