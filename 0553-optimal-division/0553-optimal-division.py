class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        elif n == 2:
            return f"{nums[0]}/{nums[1]}"
        else:
            return f"{nums[0]}/({'/'.join(map(str, nums[1:]))})"