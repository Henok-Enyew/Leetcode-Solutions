# Problem: Broken Keyboard - https://codeforces.com/problemset/problem/1251/A

t = int(input())
for _ in range(t):
    s = input().strip()
    working = set()
    n = len(s)
    i = 0
    while i < n:
        if i == n - 1 or s[i] != s[i+1]:
            working.add(s[i])
            i += 1
        else:
            i += 2
    print(''.join(sorted(working)))