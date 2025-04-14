# Problem: E - Skibidus and Sigma - https://codeforces.com/gym/603156/problem/E

import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, m = map(int, input[ptr:ptr+2])
        ptr += 2
        arrays = []
        sums = []
        for _ in range(n):
            arr = list(map(int, input[ptr:ptr+m]))
            ptr += m
            arrays.append(arr)
            sums.append(sum(arr))
        paired = sorted(zip(sums, arrays), key=lambda x: -x[0])
        concatenated = []
        for sum_val, arr in paired:
            concatenated.extend(arr)
        total_score = 0
        prefix_sum = 0
        for i in range(len(concatenated)):
            prefix_sum += concatenated[i]
            total_score += prefix_sum
        print(total_score)

solve()