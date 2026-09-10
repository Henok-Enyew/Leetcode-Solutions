class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        temp = []
        low = 0
        high = len(s)

        for i in range(len(s)):
            if s[i] == 'I':
                temp.append(low)
                low += 1
            else:
                temp.append(high)
                high -= 1

        temp.append(high)
        return temp