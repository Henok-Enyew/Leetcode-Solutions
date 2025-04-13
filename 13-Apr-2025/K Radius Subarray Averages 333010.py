# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)

        ans = []
        left = 0
        end = k*2
        sm = sum(nums[:end])
        for right in range(l):
            if right < k or right > l - k - 1:
                ans.append(-1)
            else:
                sm += nums[end]
                a = math.floor( sm / (k * 2 + 1) )
                ans.append(a)
                sm -= nums[left]
                end += 1
                left += 1
        return ans

            