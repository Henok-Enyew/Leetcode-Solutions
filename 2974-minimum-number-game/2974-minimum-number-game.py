class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        numSorted = sorted(nums)
        arr = []
        i = 0
        while(i < len(nums) -1):
            arr.append(numSorted[i+1])
            arr.append(numSorted[i ])
            i += 2
        return arr
