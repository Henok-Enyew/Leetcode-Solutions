from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Initialize a set to keep track of numbers seen in A and B
        seen = set()
        # Initialize the prefix common array
        C = []
        # Counter for common elements
        common_count = 0

        # Iterate through the arrays
        for i in range(len(A)):
            # Add current elements from A and B to the seen set
            if A[i] in seen:
                common_count += 1
            else:
                seen.add(A[i])

            if B[i] in seen:
                common_count += 1
            else:
                seen.add(B[i])

            # Append the current common count to the result array
            C.append(common_count)

        return C
