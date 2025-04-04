class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix , prefix, answer = [], [], []
        product = 1
        for n in nums:
            product *= n
            prefix.append(product)
        product = 1
        for i in range(len(nums)-1,-1,-1):
            product *= nums[i]
            suffix.append(product)
        suffix.reverse()
        answer.append(suffix[1])
        for i in range(1,len(nums)-1):
            ans = prefix[i-1] * suffix[i + 1]
            answer.append(ans)
        answer.append(prefix[-2])
        return answer