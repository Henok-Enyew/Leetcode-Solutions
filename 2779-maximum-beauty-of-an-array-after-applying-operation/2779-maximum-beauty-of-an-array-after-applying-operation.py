class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Sort the nums array to facilitate a sliding window approach
        nums.sort()
        
        max_beauty = 0
        left = 0
        
        # Use a sliding window to find the maximum beauty
        for right in range(len(nums)):
            # Adjust the window to ensure all elements fall within the range
            while nums[right] - nums[left] > 2 * k:
                left += 1
            # Calculate the length of the current valid window
            max_beauty = max(max_beauty, right - left + 1)
        
        return max_beauty
