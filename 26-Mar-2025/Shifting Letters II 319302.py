# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        st = []
        prefix_sum = [0] * len(s)
        for shift in shifts:
            start, right, direction = shift
            if direction == 1:
                prefix_sum[start] += 1
            else:
                prefix_sum[start] -= 1
            if right + 1 < n:
                prefix_sum[right+1] -=1 if direction == 1 else -1 
        acc = 0
        for i in range(len(s)):
            acc += prefix_sum[i]
            new_char = (ord(s[i]) - 97 + acc) % 26 + 97
            st.append(chr(new_char))
        return ''.join(st)