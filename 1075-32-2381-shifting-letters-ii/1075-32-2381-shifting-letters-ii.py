class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_array = [0] * (n + 1)  # To apply range updates
        
        for start, end, direction in shifts:
            if direction == 1:  # Forward shift
                shift_array[start] += 1
                shift_array[end + 1] -= 1
            else:  # Backward shift
                shift_array[start] -= 1
                shift_array[end + 1] += 1
        
        current_shift = 0
        result = []
        for i in range(n):
            current_shift += shift_array[i]
            new_char = chr((ord(s[i]) - ord('a') + current_shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)
