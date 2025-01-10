class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        from collections import Counter
        
        # Compute the maximum character frequencies required by words2
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char, freq in word_count.items():
                max_freq[char] = max(max_freq[char], freq)
        
        # Filter words in words1 that satisfy the universal condition
        result = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= max_freq[char] for char in max_freq):
                result.append(word)
        
        return result
