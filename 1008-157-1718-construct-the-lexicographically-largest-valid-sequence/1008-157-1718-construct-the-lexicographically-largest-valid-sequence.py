from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        res = [0] * size
        used = set()

        def backtrack(index):
            if index == size:
                return True
            
            if res[index] != 0:
                return backtrack(index + 1)
            
            for num in range(n, 0, -1):
                if num in used:
                    continue
                
                if num == 1:
                    res[index] = num
                    used.add(num)
                    if backtrack(index + 1):
                        return True
                    res[index] = 0
                    used.remove(num)
                else:
                    if index + num < size and res[index + num] == 0:
                        res[index] = res[index + num] = num
                        used.add(num)
                        if backtrack(index + 1):
                            return True
                        res[index] = res[index + num] = 0
                        used.remove(num)
            
            return False
        
        backtrack(0)
        return res
