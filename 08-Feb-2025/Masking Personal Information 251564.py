# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        answer = ''
        indexofAt = s.find('@')
        if indexofAt !=-1:
            answer = f"{s[0]}*****{s[indexofAt - 1]}{s[indexofAt:]}".lower()
        else:
            answer = s
            for i in ['+', '-', '(', ')', ' ']:
                answer = answer.replace(i,'')
            print(answer)
            if len(answer)==10:
                answer = f"***-***-{answer[-4:]}"
            else:
                answer = f"+{'*'*(len(answer)-10)}-***-***-{answer[-4:]}"
        return answer