class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedArr = sorted(score, reverse=True)
        map = {}
        answer = []
        for i,s in enumerate( sortedArr):
            if i==0:
                map[s] = "Gold Medal"
            elif i == 1:
                map[s] = "Silver Medal"
            elif i==2:
                map[s] = "Bronze Medal"
            else:
                map[s] = f"{i+1}"
        for s in score:
            answer.append(map[s])
        return answer
