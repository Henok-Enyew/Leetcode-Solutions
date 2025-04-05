class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        store = 0
        for i in range(len(people)):
            cur = people[i]
            if store:
                if store + cur <= limit:
                    boats+=1
                else:
                    boats+=2
                store=0
            else:
                if cur < limit:
                    store = cur
                if cur == limit or i == len(people) - 1:
                    boats+=1
            print(cur,boats)
        return boats