class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        
        # Helper function to check if a substring is special
        def is_special(sub: str) -> bool:
            return len(set(sub)) == 1
        
        for length in range(n, 0, -1):  # Start from longest substring
            seen = {}
            
            for i in range(n - length + 1):  # Generate all substrings of `length`
                substring = s[i:i + length]
                if is_special(substring):
                    if substring in seen:
                        seen[substring] += 1
                    else:
                        seen[substring] = 1
            
            # Check if any substring occurs at least 3 times
            for count in seen.values():
                if count >= 3:
                    return length
        
        return -1
