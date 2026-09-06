class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack=[]
        n=len(nums)
        for i in range(n):
            while len(stack) and stack[-1]>nums[i]:
                if (n-1-i)>=k-len(stack):
                    stack.pop()
                else:
                    break
            stack.append(nums[i])
        return stack[:k]