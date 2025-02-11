# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        lookup = collections.Counter(nums)
        pairs=0
        leftovers=0
        for key in lookup:
            if lookup[key] %2 == 0:
                pairs+= int(lookup[key] /2)
            else:
                if lookup[key] == 1:
                    leftovers+=1
                else:
                    pairs+=math.floor(lookup[key]/2)
                    leftovers+=1
        print(lookup)
        return [pairs,leftovers]