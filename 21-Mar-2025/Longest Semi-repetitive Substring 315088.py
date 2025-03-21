# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        N = len(s)
        answer = 1
        count  = 0
        left = 0
        for right in range(1,N):
            if s[right] == s[right - 1]:
                count += 1
            while count > 1:
                if s[left] == s[left+1]:
                    count -= 1
                left+=1
            answer = max(answer, right - left + 1)
        return answer