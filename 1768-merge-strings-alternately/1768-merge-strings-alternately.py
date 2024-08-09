class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = len(word1) if len(word1) > len(word2) else len(word2)
        result = []
        for i in range(length):
            if len(word1) > i:
                result.append(word1[i])
            if len(word2) > i:
                result.append(word2[i])
        return "".join(result)
