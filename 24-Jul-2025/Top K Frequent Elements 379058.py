# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        
        a = Counter(nums)

        
        ta = sorted(a.items(), key=lambda item: item[1], reverse=True)

        
        for i in range(k):
            
            ans.append(ta[i][0])
            
        return ans
