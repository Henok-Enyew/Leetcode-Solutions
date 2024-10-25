class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            if num %2 == 0:
                answer.insert(0,num)
            else:
                answer.append(num)
        return answer