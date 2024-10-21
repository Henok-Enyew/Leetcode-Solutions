from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        magaz = Counter(magazine)
 
        for n in ransom.keys():
            if n not in magaz.keys():
                return False
            else:
                if ransom[n] > magaz[n]:
                    return False
        return True
