# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_post  = {char: i for i, char in enumerate(s)}

        stack = []

        seen = set()

        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i] < stack[-1] and i < last_post[stack[-1]]:
                    seen.discard(stack.pop())
                stack.append(s[i])
                seen.add(s[i])
        return "".join(stack)