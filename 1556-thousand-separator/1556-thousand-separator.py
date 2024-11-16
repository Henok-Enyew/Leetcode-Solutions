class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        answer = ''
        counter = 0
        if len(s) <4:
            return s
        for i in range(len(s)-1,-1,-1):
            if counter %3 == 0 and counter !=0:
                answer = '.'+answer
                counter = 0
            answer= s[i] + answer
            counter +=1

            
        return answer
            