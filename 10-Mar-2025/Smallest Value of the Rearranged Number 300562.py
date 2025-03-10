# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        isNegative = num < 0
        str_num = str(num)
        if (len(str_num) == 1):
            return int(str_num)
        numberofzeros = str_num.count('0')
        arrnum = list( str_num)
        if isNegative:
            arrnum.sort(reverse=True)
        else:
            arrnum.sort()
        arrnum = list(filter(lambda x: x != '0' and x != '-' ,arrnum))
        str_num = ''
        for st in arrnum[1:]:
            str_num += st
        str_num = str(arrnum[0]) + '0' * numberofzeros + str_num if not isNegative else str(arrnum[0]) + str_num + '0' * numberofzeros
        answer = -1 * int(str_num) if isNegative else int(str_num)
        return answer