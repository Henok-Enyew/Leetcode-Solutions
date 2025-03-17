# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        l=len(arr)
        while i<l:
            if arr[i] == 0:
                arr.insert(i,0)
                i+=2
            else:
                i+=1
        while l < len(arr):
            arr.pop()