# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

from collections import Counter 
t = int(input())
while t:
    t-=1
    length = int(input())
    numbers = list(map(int, input().split()))
    cnt = Counter()
    ans = 0
    for i, x in enumerate(numbers):
        ans += i - cnt[i - x]
        cnt[i - x] += 1
    n = len(numbers)
    ans = (n * (n - 1) // 2) - ans
    print(ans)
