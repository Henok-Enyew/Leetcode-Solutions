# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            print(*arr)
            j -= 1
        
        arr[j + 1] = key    
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().split()))
    insertionSort1(n, arr)
