# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for l in logs:
            if l == '../' :
                if count > 0:
                    count -= 1
            elif l == './':
                continue
            else:
                count += 1
        return count if count >=0 else 0    