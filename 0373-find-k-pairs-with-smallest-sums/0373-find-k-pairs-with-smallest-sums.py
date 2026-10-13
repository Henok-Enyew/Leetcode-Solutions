from heapq import heappop, heappush
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        list_length = len(nums1)
        min_heap = []
        pairs = []

        for i in range(min(k, list_length)):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        counter = 1

        while min_heap and counter <= k:
            sum_of_pairs, i, j = heappop(min_heap)

            pairs.append([nums1[i], nums2[j]])

            next_element = j + 1

            if len(nums2) > next_element:
                heappush(min_heap, (nums1[i] + nums2[next_element], i, next_element))

            counter += 1

        return pairs