# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        answer = []
        for st in strs:
            sorted_st = ''.join(sorted(st))
            if sorted_st not in mp:
                mp[sorted_st] = st
            else:
                mp[sorted_st] = f"{mp[sorted_st]} {st}"
                
        print(mp)
        for m in mp:
            ans = []
            for ms in mp[m].split(' '):
                
                ans.append(ms)
            answer.append(ans)
        return answer
        