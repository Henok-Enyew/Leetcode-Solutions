# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        transform = "" 
        for st in s:
            transform += str(ord(st) - 96)
        while k > 0 and len(transform) > 1:
            acc = 0
            for tr in transform:
                acc += int(tr)
            transform = str(acc)
            k -= 1
        return int(transform)     