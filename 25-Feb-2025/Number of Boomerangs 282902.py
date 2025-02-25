# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def get_dist(a,b):
            return (a[0] - b[0])**2 + (a[1]-b[1])**2
        
        count = 0
        for i , n in enumerate(points):
            d = collections.defaultdict(int)
            for j,m in enumerate(points):
                if i == j:
                    continue
                distance = get_dist(n,m)
                d[distance] +=1
            for k in d.keys():
                count += d[k] * (d[k]-1)
        return count
