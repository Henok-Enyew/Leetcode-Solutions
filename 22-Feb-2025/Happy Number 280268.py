# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        mp = {}
        num = str(n)
        result = 0
        while True:
            for j in num:
                result += int(j)**2
            
            num = str(result)
            if result in mp:
                return False
            mp[result] = 'seen'
            if result == 1:
                return True
            result = 0