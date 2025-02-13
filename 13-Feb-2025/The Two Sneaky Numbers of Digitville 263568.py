# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        mp = collections.Counter(nums)
        answer = []
        for k in mp.keys():
            if mp[k] >1:
                answer.append(k)
        return answer