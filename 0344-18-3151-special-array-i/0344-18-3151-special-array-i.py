class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def isEven(num):
            return num %2 == 0
        
        for i in range(1,len(nums)):
            if isEven(nums[i]) == isEven(nums[i-1]):
                return False
        return True