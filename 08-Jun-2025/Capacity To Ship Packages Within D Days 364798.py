# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def black_box(self, capacity, weights, given_days):
        curr_capacity = 0
        W = len(weights)
        days_cout = 1
        #########
        for index in range(W):
            if curr_capacity + weights[index] > capacity:
                curr_capacity = weights[index]
                days_cout += 1
            else:
                curr_capacity += weights[index]

        return days_cout > given_days




    def shipWithinDays(self, weights: List[int], days: int) -> int:


        low = max(weights)
        high = sum(weights)

        ans = high


        while low <=high:
            capacity = (low + high) // 2
            if self.black_box(capacity, weights, days):
                low = capacity + 1
            else:
                ans = min(capacity, ans)
                high = capacity - 1
##############
        return ans