from typing import List
import bisect

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort events by end time
        events.sort(key=lambda x: x[1])  # Sort by endTime
        max_value = 0
        prefix_max = []  # To store the max value seen so far
        
        # Step 2: Prepare for binary search by extracting end times and max values
        end_times = []
        for event in events:
            end_times.append(event[1])
            max_value = max(max_value, event[2])
            prefix_max.append(max_value)
        
        # Step 3: Iterate through events and compute the maximum sum
        max_sum = 0
        for start, end, value in events:
            # Find the best non-overlapping event using binary search
            idx = bisect.bisect_left(end_times, start) - 1
            best_non_overlap = prefix_max[idx] if idx >= 0 else 0
            
            # Compute the max sum for the current event
            max_sum = max(max_sum, value + best_non_overlap)
        
        return max_sum
