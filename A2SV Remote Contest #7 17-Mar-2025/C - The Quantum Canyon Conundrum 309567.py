# Problem: C - The Quantum Canyon Conundrum - https://codeforces.com/gym/596004/problem/C

def is_true_canyon(n, a):
    segments = []
    i = 0
    while i < n:
        current = a[i]
        start = i
        while i < n and a[i] == current:
            i += 1
        end = i - 1
        segments.append((start, end, current))
    
    valid_segments = []
    for seg in segments:
        l, r, val = seg
        left_cond = (l == 0) or (a[l - 1] > val)
        right_cond = (r == n - 1) or (a[r + 1] > val)
        if left_cond and right_cond:
            valid_segments.append(seg)
    
    return len(valid_segments) == 1

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if is_true_canyon(n, a):
        print("YES")
    else:
        print("NO")