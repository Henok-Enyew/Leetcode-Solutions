from collections import Counter
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)
        max_heap = [(-ord(char), freq) for char, freq in count.items()]
        heapq.heapify(max_heap)
        result = []
        prev_char = None  
        prev_count = 0    
        while max_heap:
            neg_char, freq = heapq.heappop(max_heap)
            char = chr(-neg_char)
            if prev_char != char or prev_count < repeatLimit:
                to_add = min(repeatLimit, freq)
                result.append(char * to_add)
                prev_char = char
                prev_count = to_add
                if freq > to_add:
                    heapq.heappush(max_heap, (neg_char, freq - to_add))
            else:
                if not max_heap:  
                    break
                next_neg_char, next_freq = heapq.heappop(max_heap)
                next_char = chr(-next_neg_char)
                result.append(next_char)
                prev_char = next_char
                prev_count = 1
                if next_freq > 1:
                    heapq.heappush(max_heap, (next_neg_char, next_freq - 1))
                heapq.heappush(max_heap, (neg_char, freq))        
        return ''.join(result)
