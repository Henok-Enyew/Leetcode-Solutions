class Solution:
    def heightChecker(self, arr: List[int]) -> int:
        copy = arr[:]
        n = len(arr)
        counter = 0
        if n <= 1:
            return 
        for i in range(1, n):
            key = arr[i]  
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        for i in range(n):
            if copy[i] != arr[i]:
                counter += 1
        return counter