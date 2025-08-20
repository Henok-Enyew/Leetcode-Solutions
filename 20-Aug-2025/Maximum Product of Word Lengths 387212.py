# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        l = len(words)
        sets = [None] * l
        lengths = [None] * l

        def get_set(c):
            s = set()
            for t in c:
                s.add(t)
            return s
        for i in range(l):
            sets[i] = get_set(words[i])
            lengths[i] = len(words[i])
        best = 0
        for i in range(l):
            for j in range(l):
                if len(sets[i] & sets[j]) == 0:
                    best = max(best,  lengths[j]* lengths[i])
        return best