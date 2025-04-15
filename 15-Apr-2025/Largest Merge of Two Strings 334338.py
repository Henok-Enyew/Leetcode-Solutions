# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1 = w2 = 0
        l1, l2 = len(word1), len(word2)
        merge = ''
        while w1 < l1 and w2 < l2:
            if word1[w1:] >= word2[w2:]:
                merge += word1[w1]
                w1 += 1
            else:
                merge += word2[w2]
                w2 += 1
        merge += word2[w2:]
        merge += word1[w1:]
        return merge