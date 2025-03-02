class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mp = {}
        answer = []
        for num in nums1:
            mp[num[0]] = num[1] 
        for num in nums2:
            if num[0] in mp:
                mp[num[0]] += num[1] 
            else:
                mp[num[0]] = num[1]
        for id in mp.keys():
            answer.append([id,mp[id]])
        answer.sort()
        return answer