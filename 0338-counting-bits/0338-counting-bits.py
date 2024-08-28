class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            b = list(bin(i)[2:]).count('1')
            answer.append(b)
        return answer