from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums) 
        odds=[]
        evens=[]
        for num in nums:
            if num %2 == 0:
                evens.append(num)
            elif num %2 != 0:
                odds.append(num)
        i = 0
        j = 1

        for even in evens:
            answer[i] = even
            i += 2

        for odd in odds:
            answer[j] = odd
            j += 2
        return answer