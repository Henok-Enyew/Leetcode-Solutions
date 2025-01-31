# Problem: Sum - https://codeforces.com/contest/1742/problem/A

import sys
input = sys.stdin.read

data = input().splitlines()
n = int(data[0])

for i in range(1, n + 1):
    a, b, c = map(int, data[i].split())
    if a + b == c or a + c == b or b + c == a:
        print("YES")
    else:
        print("NO")