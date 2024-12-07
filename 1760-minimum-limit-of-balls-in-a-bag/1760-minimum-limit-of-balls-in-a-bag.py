class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canDivide(mid):
            operations = 0
            for num in nums:
                if num > mid:
                    operations += (num - 1) // mid  # Calculate the required splits
            return operations <= maxOperations

        left, right = 1, max(nums)  # Penalty range
        result = right

        while left <= right:
            mid = (left + right) // 2
            if canDivide(mid):
                result = mid  # Update the result if valid
                right = mid - 1  # Try for a smaller penalty
            else:
                left = mid + 1  # Increase the penalty
        
        return result
