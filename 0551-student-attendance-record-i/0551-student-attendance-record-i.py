class Solution:
    def checkRecord(self, s: str) -> bool:
        late = 0
        absent = 0
        islate = False
        for i in range(len(s)):
            if absent >= 2 or late >= 3:
                return False
            if s[i] == 'A':
                absent+=1
                islate = False
            elif s[i] == 'L':
                if islate:
                    late +=1
                else:
                    late=1
                    islate = True
            else:
                islate = False
                late = 0
        print(late)

        return absent < 2 and late < 3