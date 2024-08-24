class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        arr = list(word)
        index = arr.index(ch)
        start = 0
        end = index
        while start <= end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end]= temp
            start +=1
            end-=1
        return "".join(arr)