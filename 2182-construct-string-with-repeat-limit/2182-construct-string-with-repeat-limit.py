from collections import Counter
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Step 1: Count frequencies of all characters
        count = Counter(s)
        
        # Step 2: Use a max-heap to store characters and their counts
        # Negate the ASCII value to simulate a max-heap behavior
        max_heap = [(-ord(char), freq) for char, freq in count.items()]
        heapq.heapify(max_heap)
        
        result = []
        prev_char = None  # To track the last added character
        prev_count = 0    # To track the number of times the previous character was added
        
        while max_heap:
            # Pop the character with the largest lexicographical order
            neg_char, freq = heapq.heappop(max_heap)
            char = chr(-neg_char)
            
            # Case 1: If the previous character is different or we haven't hit the limit
            if prev_char != char or prev_count < repeatLimit:
                # Append the character up to min(repeatLimit, freq) times
                to_add = min(repeatLimit, freq)
                result.append(char * to_add)
                
                # Update previous character and its count
                prev_char = char
                prev_count = to_add
                
                # If there are remaining characters, push them back into the heap
                if freq > to_add:
                    heapq.heappush(max_heap, (neg_char, freq - to_add))
            
            # Case 2: If the previous character has reached the repeatLimit
            else:
                if not max_heap:  # If no other characters are available, break
                    break
                
                # Use the next largest character as a spacer
                next_neg_char, next_freq = heapq.heappop(max_heap)
                next_char = chr(-next_neg_char)
                result.append(next_char)
                
                # Update previous character and its count
                prev_char = next_char
                prev_count = 1
                
                # Push back the used character with decremented frequency
                if next_freq > 1:
                    heapq.heappush(max_heap, (next_neg_char, next_freq - 1))
                
                # Push the current character back as well
                heapq.heappush(max_heap, (neg_char, freq))
        
        return ''.join(result)
