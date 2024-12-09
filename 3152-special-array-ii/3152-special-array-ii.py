class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        # Handle edge case for single-element array
        if n == 1:
            return [query[0] == query[1] for query in queries]

        # Precompute parity changes
        parity_changes = [0] * (n - 1)
        for i in range(n - 1):
            parity_changes[i] = (nums[i] % 2) == (nums[i + 1] % 2)  # 1 if same parity, 0 otherwise

        # Prefix sum of parity changes
        prefix_sum = [0] * (n - 1)
        prefix_sum[0] = parity_changes[0]
        for i in range(1, n - 1):
            prefix_sum[i] = prefix_sum[i - 1] + parity_changes[i]

        # Helper to calculate range sum
        def get_range_sum(left: int, right: int) -> int:
            if left > right:
                return 0
            return prefix_sum[right] - (prefix_sum[left - 1] if left > 0 else 0)

        # Evaluate each query
        result = []
        for fromi, toi in queries:
            if toi == fromi:  # Single element subarray is always special
                result.append(True)
            else:
                # Check if there are any parity mismatches in the range
                result.append(get_range_sum(fromi, toi - 1) == 0)
        
        return result
