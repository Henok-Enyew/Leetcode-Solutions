# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class MapSum:

    def __init__(self):
        self.Map = defaultdict(int)
        self.visit = set()
        self.key = {}

    def insert(self, key: str, val: int) -> None:
        cur = ""
        for i in key:
            cur += i
            if key in self.key:
                self.Map[cur] -= self.key[key]
            self.Map[cur] += val

        self.visit.add(key)
        self.key[key] = val

    def sum(self, prefix: str) -> int:
        return self.Map[prefix]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)