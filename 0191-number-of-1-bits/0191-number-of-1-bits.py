class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        num = 0
        while True:
            if n==1:
                counter += 1
                break
            num = n%2
            n//=2
            if num == 1:
                counter += 1
        return counter
