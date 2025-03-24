class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        length = len(arr)
        l,r =0,1
        best,prev = 1, ''
        while r<length:
            if arr[r-1] > arr[r] and prev != '>':
                best = max(best, r-l+1)
                r+=1
                prev = '>'
            elif arr[r-1] < arr[r] and prev != '<':
                best = max(best, r-l+1)
                r+=1
                prev = '<'
            else:
                r = r+1 if arr[r] == arr[r-1] else r
                l = r - 1
                prev=''
        return best