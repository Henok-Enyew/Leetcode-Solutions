# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        answer = []
        l = len(img)
        for i in range(l):
            answer.append([])
            for j in range(len(img[0])):
                count,value= 0,0
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if 0 <= i + dx < len(img) and  0 <= j + dy < len(img[0]):
                            value += img[i+dx][j+dy]
                            count +=1
                answer[-1].append(value // count)
        return answer


            
