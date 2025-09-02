# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        i = 0
        
        while i<len(arr):
            mi = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[mi]:
                    mi = j 

            arr[mi], arr[i] = arr[i], arr[mi]
            i+=1
        return arr
            
            