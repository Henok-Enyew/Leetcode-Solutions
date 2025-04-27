# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
a = list(map(int, input().split()))
has_even = any(x % 2 == 0 for x in a)
has_odd = any(x % 2 == 1 for x in a)
if has_even and has_odd:
    a.sort()
print(' '.join(map(str, a)))