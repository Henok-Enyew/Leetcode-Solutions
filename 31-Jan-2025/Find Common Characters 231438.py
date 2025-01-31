# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        output = {}
        answer = []
        for s in words[0]:
            if s in output.keys():
                output[s] += 1
            else:
                output[s] = 1
        for i in range(1,len(words)):
            newmap = {}
            for s in words[i]:
                if s in newmap.keys():
                    newmap[s] += 1
                else:
                    newmap[s] = 1
            print(newmap)
            for o in output.keys():
                if o not in newmap.keys():
                    print(o)
                    output[o] = 0
                else:
                    output[o] = min(output[o], newmap[o])
        for k in output.keys():
            i = 0
            for i in range(output[k]):
                answer.append(k)
        return answer
                    