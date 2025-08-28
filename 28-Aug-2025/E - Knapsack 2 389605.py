# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

import sys
input = sys.stdin.readline

def main():
    N, W = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]

    MAX_V = N * 1000
    INF = 10**18
    dp = [INF] * (MAX_V + 1)
    dp[0] = 0

    for w, v in items:
        for val in range(MAX_V, v - 1, -1):
            if dp[val - v] + w < dp[val]:
                dp[val] = dp[val - v] + w

    ans = 0
    for val in range(MAX_V + 1):
        if dp[val] <= W:
            ans = val
    print(ans)

if __name__ == "__main__":
    main()
