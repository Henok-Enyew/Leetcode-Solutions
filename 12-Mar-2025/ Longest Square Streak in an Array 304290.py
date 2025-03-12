# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        mp = collections.Counter(nums)
        maxstreak = -1
        counter = 0 
        for num in nums:
            n = num
            while n*n in mp:
                n=n*n
                counter+=1
            if counter:
                maxstreak = max(maxstreak,counter+1)
            counter = 0
        return maxstreak
        
