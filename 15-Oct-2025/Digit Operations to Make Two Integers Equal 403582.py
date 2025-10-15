# Problem: Digit Operations to Make Two Integers Equal - https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        def get_digits(num):
            return [int(d) for d in str(num)]
        
        def to_number(digits):
            return int(''.join(map(str, digits)))
        
        if is_prime(m):
            return -1
        
        if is_prime(n):
            return -1
        
        pq = [(n, n)]  # (cost, start number)
        visited = {n: n}  # set or map to speed the like dist in dijstkra
                
        while pq:
            curr_cost, curr_num = heappop(pq)
            
            
            if curr_num == m:
                return curr_cost
            
            digits = get_digits(curr_num)
            
            for i in range(len(digits)):
                if digits[i] < 9:
                    new_digits = digits.copy()
                    new_digits[i] += 1
                    new_num = to_number(new_digits)
                    
                    if not is_prime(new_num):
                        new_cost = curr_cost + new_num
                        if new_num not in visited or new_cost < visited[new_num]:
                            visited[new_num] = new_cost
                            heappush(pq, (new_cost, new_num))
                
                if digits[i] > 0:
                    new_digits = digits.copy()
                    new_digits[i] -= 1
                    new_num = to_number(new_digits)
                    
                    if not is_prime(new_num):
                        new_cost = curr_cost + new_num
                        if new_num not in visited or new_cost < visited[new_num]:
                            visited[new_num] = new_cost
                            heappush(pq, (new_cost, new_num))
        
        return -1