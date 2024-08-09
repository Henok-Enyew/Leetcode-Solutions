class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            if op == "C" and len(scores) != 0:
                scores.pop()
            elif op == "+":
                sum = int(scores[-1]) + int(scores[-2])
                scores.append(sum)
            elif op == "D":
                scores.append(int(scores[-1]) * 2)
            else:
                scores.append(int(op))
        totalScore = 0
        for score in scores:
            totalScore += score
        return totalScore