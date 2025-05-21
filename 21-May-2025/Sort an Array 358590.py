# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, s, m, e):
            L = arr[s: m + 1]
            R = arr[m + 1: e + 1]
            i = 0 
            j = 0 
            k = s 
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        def mergeSort(arr, s, e):
            if e - s + 1 <= 1 :
                return arr
            m = (e+s) //2
            left = mergeSort(arr,s,m)
            right = mergeSort(arr,m+1, e)
            merge(arr, s,m,e)
            return arr
        
        return mergeSort(nums,0, len(nums) -1 )