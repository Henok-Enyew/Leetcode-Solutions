# Problem: E - Quantum Severance – A Battle of Edges - https://codeforces.com/gym/596004/problem/E

import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        a = list(map(int, input[idx:idx + n]))
        idx += n
        
        prefix_pos = [0] * (n + 1)
        for i in range(n):
            prefix_pos[i + 1] = prefix_pos[i] + (a[i] if a[i] > 0 else 0)
        
        suffix_neg = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_neg[i] = suffix_neg[i + 1] + (-a[i] if a[i] < 0 else 0)
        
        suffix_pos = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_pos[i] = suffix_pos[i + 1] + (a[i] if a[i] > 0 else 0)
        
        prefix_neg = [0] * (n + 1)
        for i in range(n):
            prefix_neg[i + 1] = prefix_neg[i] + (-a[i] if a[i] < 0 else 0)
        
        max_sum = 0
        for i in range(n + 1):
            current_sum = prefix_pos[i] + suffix_neg[i]
            if current_sum > max_sum:
                max_sum = current_sum
        
        max_sum = max(max_sum, suffix_pos[0], prefix_neg[n])
        
        print(max_sum)

if __name__ == "__main__":
    main()