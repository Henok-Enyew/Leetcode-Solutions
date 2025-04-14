# Problem: Day at the Beach - https://codeforces.com/problemset/problem/599/C

n = int(input())
h = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()

prefix_max = [0] * n
prefix_max[0] = h[0]
for i in range(1, n):
    prefix_max[i] = max(prefix_max[i-1], h[i])

suffix_min = [0] * n
suffix_min[-1] = h[-1]
for i in range(n-2, -1, -1):
    suffix_min[i] = min(suffix_min[i+1], h[i])

count = 0
for i in range(n-1):
    if prefix_max[i] <= suffix_min[i+1]:
        count += 1

print(count + 1)