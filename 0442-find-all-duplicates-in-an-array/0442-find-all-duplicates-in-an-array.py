class Solution:
    def findDuplicates(self, num: List[int]) -> List[int]:
        map={}
        answer=[]
        for i in range(len(num)):
            if num[i] in map.keys():
                answer.append(num[i])
            else:
                map[num[i]] = 1
        return answer