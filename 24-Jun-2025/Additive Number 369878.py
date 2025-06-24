# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        N = len(num)
        def calc(first, second):
            p = [str(first), str(second)]
            total = sum(len(x) for x in p)

            while total < N:
                p.append(str(int(p[-1]) + int(p[-2])))
                total += len(p[-1])
            return "".join(p)
        for left in range(1, N):
            for right in range(left+1,N):
                if num[left] == "0" and right - left > 1:
                    break
                first = int(num[:left])
                second = int(num[left:right])

                s = calc(first,second)
                if s == num:
                    return True
            if num[0]=='0':
                break
        return False
