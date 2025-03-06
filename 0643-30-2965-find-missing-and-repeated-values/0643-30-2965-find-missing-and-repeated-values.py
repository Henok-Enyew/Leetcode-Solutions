class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        lookup = {k:1 for k in range(1,len(grid) * len(grid )+1) }
        store = {}
        answer = []
        for gr in grid:
            for g in gr:
                if g in store:
                    answer.append(g)
                else:
                    store[g]=1
        print(store)
        # print(lookup)
        print(answer)
        for l in lookup.keys():
            if l not in store:
                answer.append(l)          
        return answer