class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = Counter()
        arr3 =[]
        answer = []
        for i in range(len(arr1)):
            if arr1[i] in arr2:
                mp[arr1[i]] +=1
            else:
                arr3.append(arr1[i])
        j = 0
        for i in range(len(arr2)):
            rep = mp[arr2[i]]
            for _ in range(rep):
                answer.append(arr2[i])
        arr3.sort()
        return answer + arr3
