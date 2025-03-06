# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

if k == 0:
    if numbers[0] > 1:
        print(numbers[0] - 1)
    else:
        print(-1)
else:
    x = numbers[k - 1]  
    if k < n and numbers[k] == x:
        print(-1)
    else:
        print(x)
