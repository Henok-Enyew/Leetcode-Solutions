# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        freq = Counter(words)
        sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        return [word for word, count in sorted_words[:k]]