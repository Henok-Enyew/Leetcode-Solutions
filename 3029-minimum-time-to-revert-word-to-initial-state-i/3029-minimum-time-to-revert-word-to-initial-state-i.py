class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        
        for ans in range(1, n // k + 1):
            if word.startswith(word[ans * k:]):
                return ans

        return n // k + 1