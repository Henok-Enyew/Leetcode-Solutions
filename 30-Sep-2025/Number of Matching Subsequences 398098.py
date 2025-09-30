# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        char_to_indices = defaultdict(list)
        for index, char in enumerate(s):
            char_to_indices[char].append(index)
        def is_subsequence(word):
            curr_pos = -1
            for c in word:
                indices = char_to_indices[c]
                i = bisect_right(indices, curr_pos)
                if i == len(indices):
                    return False
                curr_pos = indices[i]
            return True
        return sum(1 for word in words if is_subsequence(word))