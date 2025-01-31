class Solution:
    def reverseWords(self, s: str) -> str:
        s_arr = s.split()
        s_arr_rev = s_arr[::-1]
        return ' '.join(s_arr_rev)