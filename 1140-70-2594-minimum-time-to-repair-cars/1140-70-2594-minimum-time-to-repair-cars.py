from typing import List
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Binary search on time
        left, right = 1, min(ranks) * (cars ** 2)

        def canRepairAll(mid: int) -> bool:
            total_cars = 0
            for r in ranks:
                total_cars += int(math.sqrt(mid // r))  # Maximum cars mechanic can repair in `mid` time
                if total_cars >= cars:
                    return True
            return False

        while left < right:
            mid = (left + right) // 2
            if canRepairAll(mid):
                right = mid  # Try a smaller time
            else:
                left = mid + 1  # Increase the time

        return left  # The minimum time required
