class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        counts = count.values()
        if math.gcd(*counts) == 1:
            return False
        return True