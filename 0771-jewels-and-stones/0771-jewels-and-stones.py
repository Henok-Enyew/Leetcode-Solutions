class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew = list(jewels)
        jewMap = collections.Counter(jew)
        numOfStones = 0
        for stone in stones:
            if stone in jewMap:
                numOfStones += jewMap[stone]
        return numOfStones