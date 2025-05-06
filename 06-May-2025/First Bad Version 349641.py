# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #
        res = None
        num = n
        up = n
        low = 0
        while True:
            res = isBadVersion(num)
            if res and not isBadVersion(num-1):
                return num
            if res:
                up = num
            else:
                low = num
            num = (low + up) // 2                