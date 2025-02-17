# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E

from collections import defaultdict
t = 1
t = int(input())
while t:
    t -= 1  
    n, k = input().split()
    n = int(n)
    k = int(k)

    a = list(map(int, input().split()))
    x = list(map(int, input().split()))

    dic = defaultdict(int) 

    for i in range(n):
        dic[abs(x[i])] += a[i] 

    f = 1
    left = 0
    for i in range(1, n + 1):  
        left += k - dic.get(i, 0)

        if left < 0:
            f = 0
            break

    if f:
        print("YES")
    else:
        print("NO")