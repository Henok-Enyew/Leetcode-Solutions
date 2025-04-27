# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n, k, q = map(int, input[ptr:ptr+3])
    ptr +=3

    max_temp = 200000
    freq = [0] * (max_temp + 2)

    for _ in range(n):
        l, r = map(int, input[ptr:ptr+2])
        ptr +=2
        freq[l] += 1
        if r + 1 <= max_temp:
            freq[r+1] -= 1

    # Compute prefix sum to get the count of recipes for each temperature
    count = [0] * (max_temp + 1)
    current = 0
    for i in range(1, max_temp +1):
        current += freq[i]
        count[i] = current

    # Create an array where 1 indicates admissible temperature
    admissible = [0] * (max_temp +1)
    for i in range(1, max_temp +1):
        if count[i] >= k:
            admissible[i] = 1

    # Compute prefix sum for admissible temperatures
    prefix = [0] * (max_temp +1)
    for i in range(1, max_temp +1):
        prefix[i] = prefix[i-1] + admissible[i]

    # Process queries
    output = []
    for _ in range(q):
        a, b = map(int, input[ptr:ptr+2])
        ptr +=2
        res = prefix[b] - prefix[a-1]
        output.append(str(res))

    print('\n'.join(output))

if __name__ == '__main__':
    main()