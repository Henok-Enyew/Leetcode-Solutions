class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        answer = []
        for cand in candies:
            if cand + extraCandies >= greatest:
                answer.append(True)
            else:
                answer.append(False)
        return answer