class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Total sum of the array
        left_sum = 0  # Sum of the left part
        valid_splits = 0  # Counter for valid splits

        for i in range(len(nums) - 1):  # Ensure at least one element is on the right
            left_sum += nums[i]  # Add the current element to the left sum
            right_sum = total_sum - left_sum  # Calculate the right sum
            if left_sum >= right_sum:
                valid_splits += 1

        return valid_splits
