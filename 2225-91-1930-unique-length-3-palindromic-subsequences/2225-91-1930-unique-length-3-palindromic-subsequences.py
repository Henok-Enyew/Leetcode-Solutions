class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_palindromes = set()
        last_occurrence = {}
        first_occurrence = {}

        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i

        for char in first_occurrence:
            start, end = first_occurrence[char], last_occurrence[char]
            if start < end:
                unique_chars_in_middle = set(s[start + 1:end])
                for middle_char in unique_chars_in_middle:
                    unique_palindromes.add((char, middle_char, char))

        return len(unique_palindromes)
