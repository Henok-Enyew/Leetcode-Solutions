# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxnum,index = 0,0
        for i,r in enumerate(mat):
            if r.count(1) > maxnum:
                maxnum = r.count(1)
                index = i
        return [index,maxnum]