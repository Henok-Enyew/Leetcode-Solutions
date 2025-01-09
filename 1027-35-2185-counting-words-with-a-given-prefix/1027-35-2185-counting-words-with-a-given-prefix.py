class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        preflen = len(pref)
        for i in range(len(words)):
            if(words[i][:preflen] == pref):
                count +=1
        return count
