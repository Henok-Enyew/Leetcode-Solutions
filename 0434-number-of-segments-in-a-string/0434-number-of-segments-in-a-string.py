class Solution:
    def countSegments(self, s: str) -> int:
        answer = 0
        for st in s.split(' '):
            print(st)
            if st == ' ' or st =='':
                continue
            answer+=1
        return answer