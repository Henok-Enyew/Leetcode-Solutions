# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        
        ans = ['']*len(arr)

        for i, s in enumerate(arr):

            subs = list(set(s[j:k] for j, k in 
                           combinations(range(len(s)+1),2)))
                           
            subs.sort(key = lambda x: (len(x), x))

            for sub in subs:
                if all(i == j or sub not in ss for j, ss in enumerate(arr)):
                    ans[i]=sub
                    break

        return ans