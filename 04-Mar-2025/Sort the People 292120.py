# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map = {}
        output = []
        for i in range(len(names)):
            map[heights[i]] = names[i]
        
        n = len(heights)
        for i in range(n - 1):  
            swapped = False
            for j in range(n - 1 - i):  
                if heights[j] < heights[j + 1]:  
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    swapped = True
            if not swapped:  
                break
        for h in heights:
            output.append(map[h])
        return output