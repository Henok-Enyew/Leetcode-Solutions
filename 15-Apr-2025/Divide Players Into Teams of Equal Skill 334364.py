# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        answer = 0
        sm = set()
        left , right= 0,  len(skill)-1
        while right > left:            
            prod = skill[left] * skill[right]
            s = skill[left] + skill[right]
            if left > 0 and s not in sm:
                return -1
            sm.add(s)
            answer += prod
            right -= 1
            left += 1
        return answer
