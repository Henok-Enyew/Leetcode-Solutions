class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):

            if nums[i] >0:
                break
            if i and nums[i] == nums[i-1]:
                continue
            j,k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j]+nums[k]
                if s < 0:
                    j+=1
                elif s>0:
                    k-=1
                else:
                    answer.append([nums[i],nums[j],nums[k]])
                    j,k = j+1, k-1
                    while j<k and nums[j] ==nums[j-1]:
                        j+=1
                    while j<k and nums[k] ==nums[k+1]:
                        k-=1
        return answer