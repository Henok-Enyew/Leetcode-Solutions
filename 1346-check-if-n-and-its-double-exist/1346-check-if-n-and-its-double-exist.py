class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            x = 2 * arr[i]
            if x in arr and arr.index(x) != i:
                return True
        return False