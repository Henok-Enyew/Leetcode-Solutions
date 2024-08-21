class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map = {}
        namesSorted =[]
        for i in range(len(names)):
            map[heights[i]] = names[i]
        for height in sorted(map.keys(), reverse = True):
            namesSorted.append(map[height])
        return namesSorted