# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for l in logs:
            if l == '../':
                if stack:
                    stack.pop()
            elif l == './':
                continue
            else:
                stack.append(l)
        print(stack)
        return len(stack)    