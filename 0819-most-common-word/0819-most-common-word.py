import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # words = paragraph.split(' ')
        words = re.split(r'[ ,!:\s]+', paragraph)
        map = {}
        for i in range(len(words)):
            word = re.sub(r'[^a-zA-Z\s]', '', words[i])
            word = word.lower()
            if word not in banned:
                if word not in map.keys():
                    map[word] = 1
                else:
                    map[word] += 1
        max_rep = 0
        answer = ''
        for k in map.keys():
            if map[k] > max_rep:
                answer = k
                max_rep = map[k]
        return answer
                

                