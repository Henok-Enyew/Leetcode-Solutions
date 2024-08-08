class Solution:
    def removeDuplicates(self, s: str) -> str:
        arr = []
        for i in range(len(s)):
            arr.append(s[i])
        i = 1
        while(i < len(arr)):
            if( arr[i] == arr[i-1]):
                arr.pop(i)
                arr.pop(i-1)
                i = i - 2 if i >= 2 else 0
            i+=1
        return "".join(arr)
