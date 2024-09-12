class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        answer = 0
        
        for i in range(len(words)):
            map={}
            c = 0
            for w in words[i]:
                if w not in map.keys():
                    map[w] = 1
            for k in map.keys():
                if k not in allowed:
                    break
                c+=1 
               
            answer= answer+ 1 if c==len(map.keys()) else answer
        return answer 
