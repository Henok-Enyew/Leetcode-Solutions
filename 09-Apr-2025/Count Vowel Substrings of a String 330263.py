# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        lookup = set('aeiou')
        count = 0
        for left in range(len(word)):
            st = set()
            for right in range(left,len(word)):
                if word[right] in lookup:
                    st.add(word[right])
                    if len(st) == 5:
                        count+=1
                else:
                    break
        return count
            