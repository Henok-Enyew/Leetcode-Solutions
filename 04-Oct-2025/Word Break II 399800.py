# Problem: Word Break II - https://leetcode.com/problems/word-break-ii/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        max_word_length = len(max(wordDict, key=len))
        words = set(wordDict)

        @cache
        def rec(i: int) -> list[str]:
            if i == len(s):
                return ['']

            ret = []
            for j in range(1, max(len(s) - i, max_word_length + 1)):
                if s[i:i+j] in words and (rests := rec(i+j)):
                    for rest in rests:
                        if rest:
                            ret.append(s[i:i+j] + ' ' + rest)
                        else:
                            ret.append(s[i:i+j])
            
            return ret
        
        return rec(0)