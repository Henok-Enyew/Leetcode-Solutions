# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binx = bin(x)
        biny = bin(y)
        binx = '0'*(4 - (len(binx[2:]) %4)) + binx[2:]
        biny = '0'*(4 - (len(biny[2:]) %4)) + biny[2:]
        print(binx)
        print(biny)
        count = 0
        i = len(binx)-1
        j = len(biny)-1
        while i>=0 and j>=0:
            # print(binx[i],biny[j] )
            if binx[i] != biny[j]:
                count+=1
            i-=1
            j-=1
        while i>=0:
            if binx[i] == '1':
                count+=1
            i-=1
        while j>=0:
            if biny[j] == '1':
                count+=1
            j-=1
        
        return count