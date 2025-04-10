# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
arr = list(map(int, input().split()))

l = serja = dima  = 0
r = n - 1
flag = 0
while l <= r:
    mx = 0
    if arr[l] >= arr[r]:
        mx = arr[l]
        l += 1
    else:
        mx = arr[r]
        r -= 1
    if flag %2 ==0:
        serja += mx
    else:
        dima += mx
    flag += 1
print(serja,dima)