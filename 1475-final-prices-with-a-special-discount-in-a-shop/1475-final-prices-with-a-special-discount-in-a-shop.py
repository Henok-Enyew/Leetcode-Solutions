class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        result = prices[:]
        stack = []
        
        for i in range(n):
            # Check if the current price is less than or equal to the top of the stack
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                result[index] = prices[index] - prices[i]
            # Push the current index onto the stack
            stack.append(i)
        
        return result
