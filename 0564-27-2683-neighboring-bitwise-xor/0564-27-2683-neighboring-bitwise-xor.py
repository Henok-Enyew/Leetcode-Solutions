class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        n = len(derived)
        x = 0
        for i in range(n):
            x ^= derived[i]
        return x == 0
