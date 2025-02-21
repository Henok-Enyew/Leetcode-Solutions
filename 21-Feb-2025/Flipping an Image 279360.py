# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row , col=  len(image),len(image)
        for i in range(row):
            for j in range(math.floor((col)/2)):
                temp = image[i][j]
                image[i][j] = image[i][col-j-1]
                image[i][col-j-1] = temp
        for i in range(row):
            for j in range(row):
                image[i][j] = 0 if image[i][j] == 1 else 1

        return image