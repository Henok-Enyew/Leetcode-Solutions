class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return n
        
        descents = n
        start = 0
        end = 1

        while end < len(prices):
            if prices[end] == prices[end - 1] - 1:
                descents += (end - start)
                end += 1
            else:
                start = end
                end = start + 1

        return descents