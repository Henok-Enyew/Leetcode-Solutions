from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        indexed_nums = sorted((num, i) for i, num in enumerate(nums))
        groups = []
        temp = [indexed_nums[0]]
        
        for i in range(1, n):
            if indexed_nums[i][0] - indexed_nums[i - 1][0] <= limit:
                temp.append(indexed_nums[i])
            else:
                groups.append(temp)
                temp = [indexed_nums[i]]
        groups.append(temp)
        
        result = [0] * n
        for group in groups:
            sorted_indices = sorted(group, key=lambda x: x[1])
            sorted_values = sorted(x[0] for x in group)
            for (val, (num, idx)) in zip(sorted_values, sorted_indices):
                result[idx] = val
        
        return result
