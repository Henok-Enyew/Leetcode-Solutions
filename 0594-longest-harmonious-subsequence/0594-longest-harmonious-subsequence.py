class Solution:
    def findLHS(self, nums: list[int]) -> int:
        lhs = 0
        count = {}
        for x in nums:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1    
        for x in count.keys():
            if x + 1 in count:
                lhs = max(lhs, count[x] + count[x+1])            
        return lhs