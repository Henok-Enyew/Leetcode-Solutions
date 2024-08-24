class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        map = {}
        windowSum = 0
        maxSum = 0
        start = 0

        for end in range(len(nums)):
            # Add current number to the map and window sum
            if nums[end] in map:
                # If a duplicate is found within the current window
                while nums[end] in map:
                    del map[nums[start]]
                    windowSum -= nums[start]
                    start += 1
            
            map[nums[end]] = end
            windowSum += nums[end]

            # Check if window size equals k
            if end - start + 1 == k:
                maxSum = max(maxSum, windowSum)
                
                # Slide the window
                windowSum -= nums[start]
                del map[nums[start]]
                start += 1
        
        return maxSum
