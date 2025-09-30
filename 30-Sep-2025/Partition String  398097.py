# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        parts, cur = {}, ""
        for ch in s:
            cur += ch
            if cur not in parts:
                parts[cur] = True
                cur = ""
        return list(parts.keys())