class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 0
        arr = []
        for num in nums:
            if num %2 == 0:
                even += 1
            else:
                odd+=1
        for i in range(even):
            arr.append(0)
        for i in range(odd):
            arr.append(1)
        return arr