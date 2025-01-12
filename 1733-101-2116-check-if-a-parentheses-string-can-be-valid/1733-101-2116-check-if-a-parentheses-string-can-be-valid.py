class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # If the length of the string is odd, it cannot be valid
        if len(s) % 2 != 0:
            return False

        # First pass: Check from left to right
        open_count = 0  # Track open parentheses count
        flexible_count = 0  # Track the count of '0's (flexible positions)

        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    open_count += 1
                else:  # s[i] == ')'
                    open_count -= 1
            else:
                flexible_count += 1  # Flexible can be '(' or ')'

            # If open_count becomes negative, flexible_count must compensate
            if open_count + flexible_count < 0:
                return False

        # Second pass: Check from right to left
        close_count = 0  # Track close parentheses count
        flexible_count = 0  # Reset flexible positions count

        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    close_count += 1
                else:  # s[i] == '('
                    close_count -= 1
            else:
                flexible_count += 1  # Flexible can be '(' or ')'

            # If close_count becomes negative, flexible_count must compensate
            if close_count + flexible_count < 0:
                return False

        # If both passes are successful, the string can be valid
        return True
