# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        n = len(word)
        count = 0

        for start in range(n):
            vowel_set = set()
            for end in range(start, n):
                if word[end] in vowels:
                    vowel_set.add(word[end])
                    if len(vowel_set) == 5:
                        count += 1
                else:
                    break  
        return count