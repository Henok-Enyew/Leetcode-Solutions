class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        rightProduct = [1] * (length + 1)
        leftProduct = [1] * (length +1)
        answer = [1] * (length)
        r = length -1
        l = 1
        for i,num in enumerate(nums):
            leftProduct[l] = num *  leftProduct[l -1 ] 
            rightProduct[r] = nums[r] *  rightProduct[r + 1 ] 
            l+=1
            r-=1
        leftProduct = leftProduct[1:]
        rightProduct = rightProduct[:-1]
        for i,ans in enumerate(answer):
            if(i==0):
                answer[i] = rightProduct[i+1]
            elif i==length-1:
                answer[i] = leftProduct[i-1]
            else:
                answer[i] = rightProduct[i+1] * leftProduct[i-1]
        return answer