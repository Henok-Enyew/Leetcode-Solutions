class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        prev_index = 0
        for space in spaces:
            result.append(s[prev_index:space])
            result.append(" ")
            prev_index = space
        result.append(s[prev_index:])
        return "".join(result)
