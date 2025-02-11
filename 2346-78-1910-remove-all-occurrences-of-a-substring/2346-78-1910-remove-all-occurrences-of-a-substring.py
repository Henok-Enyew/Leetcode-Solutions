class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        answer = s
        while answer.find(part) !=-1:
            startIndex = answer.find(part)
            answer = answer[:startIndex]+answer[startIndex+len(part):]
        return answer