# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

from collections import defaultdict
mp = defaultdict(list)
n = int(input())
k = int(input())
while k:
    k -= 1
    arr = list(map(int, input().split()))
    a = arr[0]
    if a == 1:
        b = arr[1]
        c = arr[2]
        mp[b].append(c)
        mp[c].append(b)
    elif a == 2:
        for v in mp[arr[1]]:
            print(str(v) + " ", end="")