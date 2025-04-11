# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        l = len(p)-1
        p_set =collections.Counter(p)
        for i in range(l-1,len(s)):
            s_set = collections.Counter(s[i-l:i+1])
            if s_set == p_set:
                answer.append(i-l)
        return answer