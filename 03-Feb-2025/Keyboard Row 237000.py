# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows={
            '1' : Counter("qwertyuiopQWERTYUIOP") ,
            '2' : Counter("asdfghjklASDFGHJKL") ,
            '3' : Counter("zxcvbnmZXCVBNM")     
        }
        output = []
        for i in range(len(words)):
            row = 1 if words[i][0] in rows['1'] else 2 if words[i][0] in rows['2'] else 3 
            areallinonerow = True
            for w in words[i]:
                if w not in rows[f"{row}"]:
                    areallinonerow = False
            if areallinonerow:
                output.append(words[i])
        return output