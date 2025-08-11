# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self,nums, target):
        store = {}
        for i in range(len(nums)):
            store[nums[i]] = i
        print(store)
        for i in range(len(nums)):
            if target - nums[i] in store and i != store[target - nums[i]]:
                return [i,store[target - nums[i]]] 