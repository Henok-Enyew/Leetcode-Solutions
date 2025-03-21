# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        left = 0
        mp = {}
        answer = 0
        for right in range(N):
            if fruits[right] not in mp:
                mp[fruits[right]] = 0
            mp[fruits[right]] += 1
            
            while len(mp) > 2:
                mp[fruits[left]] -= 1
                if mp[fruits[left]] == 0:
                    del mp[fruits[left]]
                left += 1
            
            answer = max(answer, right - left + 1)
        return answer