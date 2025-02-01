# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        answer = ['']*len(s.split())
        for st in s.split():
            answer[int(st[-1])-1] = st[:-1]
        return ' '.join(answer)