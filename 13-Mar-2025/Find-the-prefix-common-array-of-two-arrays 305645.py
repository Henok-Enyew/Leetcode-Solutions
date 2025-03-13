# Problem: Find-the-prefix-common-array-of-two-arrays - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        C = []
        common_count = 0

        for i in range(len(A)):
            if A[i] in seen:
                common_count += 1
            else:
                seen.add(A[i])

            if B[i] in seen:
                common_count += 1
            else:
                seen.add(B[i])

            C.append(common_count)

        return C
