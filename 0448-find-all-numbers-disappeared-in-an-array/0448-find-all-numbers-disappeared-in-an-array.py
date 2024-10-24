class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_map = {}
        for num in nums:
            nums_map[num] = num
        n = len(nums)
        answer = []
        m = {i:i for i in range(1, n+1)}
        for num in m.keys():
            if num not in nums_map.keys():
                answer.append(num)
        return answer