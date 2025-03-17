# Problem: D - The Snap of Fury - https://codeforces.com/gym/596004/problem/D

n = int(input())
L = list(map(int, input().split()))

intervals = []
for i in range(n):
    a = max(0, i - L[i])
    b = i - 1
    if a <= b:
        intervals.append((a, b))

intervals.sort()
merged = []
for start, end in intervals:
    if not merged:
        merged.append((start, end))
    else:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            new_start = last_start
            new_end = max(last_end, end)
            merged[-1] = (new_start, new_end)
        else:
            merged.append((start, end))

covered = 0
for start, end in merged:
    covered += end - start + 1

print(n - covered)