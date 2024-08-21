class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = [0] * len(indices) 
        for i,st in enumerate(s):
            answer[indices[i]] = st
        return "".join(answer)