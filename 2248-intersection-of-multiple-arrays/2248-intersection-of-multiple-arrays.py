class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        mapp = {}
        answer = []
        for num in nums:
            for n in set(num):
                if n not in mapp:
                    mapp[n] = 1
                else:
                    mapp[n] += 1
        for m in mapp:
            if mapp[m] == len(nums):
                answer.append(m)
                
        return sorted(answer)