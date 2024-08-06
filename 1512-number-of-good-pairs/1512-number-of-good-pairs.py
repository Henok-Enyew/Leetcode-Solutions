class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counter=0
        length = len(nums)
        for i in range(length):
            for j in range(length):
                print(i,j)
                if(nums[i] == nums[j] and i < j):
                    counter +=1
        return counter