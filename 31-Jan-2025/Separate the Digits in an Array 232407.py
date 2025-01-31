# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            n = num
            stack = []
            while n>0:
                stack.insert(0,n % 10)
                n = math.floor( n/10)
            answer += stack
        return answer