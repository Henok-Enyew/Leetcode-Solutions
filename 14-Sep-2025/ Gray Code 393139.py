# Problem:  Gray Code - https://leetcode.com/problems/gray-code/description/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        size = 1 << n 
        return [i ^ (i >> 1) for i in range(size)]