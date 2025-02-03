# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map = {}
        output = []
        for i in range(len(names)):
            map[heights[i]] = names[i]
        heights.sort(reverse=True)
        print(map)
        for h in heights:
            output.append(map[h])
        return output