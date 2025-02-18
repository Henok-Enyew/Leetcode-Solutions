class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = ""
        num = 1  # Start from '1' since we use digits from '1' to '9'
        
        for ch in pattern:
            stack.append(str(num))
            num += 1
            
            if ch == 'I':  # If 'I', pop all elements from stack
                while stack:
                    result += stack.pop()
        
        stack.append(str(num))  # Add the last number
        
        while stack:  # Pop remaining elements
            result += stack.pop()
        
        return result
