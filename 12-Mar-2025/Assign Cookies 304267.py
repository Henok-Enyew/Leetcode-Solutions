# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        p1,p2 = 0,0
        g.sort()
        s.sort()
        count=0
        while p1 < len(g) and p2 < len(s):
            if s[p2] >= g[p1]:
                count+=1
                p1+=1
                p2+=1
            elif s[p2] < g[p1]:
                p2+=1
        return count