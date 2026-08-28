class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        ans = []
        index = 0
        print(nums)
        start = nums[0]
        end = nums[len(nums) - 1]
        for i in range(start, end+1):
            if nums[index] != i:
                ans.append(i)
            else:
                index += 1
        return ans