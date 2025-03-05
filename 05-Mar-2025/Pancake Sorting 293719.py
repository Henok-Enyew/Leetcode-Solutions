# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length = len(arr)
        answer = []
        k = length
        while k>0:
            i = arr.index(k) + 1
            answer.append(i)
            answer.append(k)

            arr = arr[:i][::-1] + arr[i:]
            arr = arr[:k][::-1] + arr[k:] 
            k-=1
        return answer