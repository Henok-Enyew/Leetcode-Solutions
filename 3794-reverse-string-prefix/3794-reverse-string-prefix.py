class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        part = s[:k]
        arr = list(part)
        arr.reverse()
        new_s = "".join(arr)
        return new_s + s[k:]