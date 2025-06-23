# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 1:
            return trust[0][1]
        elif len(trust) ==0 and n == 1:
            return 1
        mp = defaultdict(list)
        for i in range(len(trust)):
            mp[trust[i][1]].append(trust[i][1])
        judge = None
        for k in mp.keys():
            if len(mp[k]) == (n -1):
                judge = k
        for i in range(len(trust)):
            if judge == trust[i][0]:
                return -1
        return judge if judge else -1