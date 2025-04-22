# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for st in s:
            if stack and st.isdigit():
                stack.pop()
            elif not st.isdigit() :
                stack.append(st)

        return ''.join(stack)