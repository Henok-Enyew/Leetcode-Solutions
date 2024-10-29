class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        max_num = max(arr)
        index = arr.index(max_num)
        if index == len(arr) -1 or index == 0:
            return False
        print(arr[index])
        for i in range(1,len(arr)):
            if i <= index:
                if arr[i-1] >= arr[i]:
                    return False
            else:
                if arr[i-1] <= arr[i]:
                    return False
        return True
                