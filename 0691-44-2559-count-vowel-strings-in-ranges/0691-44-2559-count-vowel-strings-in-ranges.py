class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel(ch):
            return ch in {'a', 'e', 'i', 'o', 'u'}
        
        n = len(words)
        prefix = [0] * (n + 1)  # prefix[i] will store the count of vowel strings up to index i-1
        
        for i in range(n):
            if is_vowel(words[i][0]) and is_vowel(words[i][-1]):
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        
        result = []
        for li, ri in queries:
            result.append(prefix[ri + 1] - prefix[li])
        
        return result
