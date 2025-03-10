# Problem: F - Luffy’s Lineup Challenge - https://codeforces.com/gym/594356/problem/F

import sys

input = sys.stdin.read
data = input().split("\n")

n = int(data[0])  # Number of crew members
a = list(map(int, data[1].split()))  # Target order
b = list(map(int, data[2].split()))  # Current order

swaps = []  # Store swap operations

pos = {val: [] for val in a}
for i in range(n):
    pos[b[i]].append(i)

for i in range(n):
    for j in range(n - 1, i, -1):
        if b[j - 1] > b[j]:  # Swap if out of order
            b[j - 1], b[j] = b[j], b[j - 1]
            swaps.append((j, j + 1))  # Store 1-based index swap

else:
    print(len(swaps))
    for swap in swaps:
        print(*swap)
