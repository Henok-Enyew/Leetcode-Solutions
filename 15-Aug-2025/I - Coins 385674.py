# Problem: I - Coins - https://atcoder.jp/contests/dp/tasks/dp_i

index = 0
n = int(input())
half = n // 2

p_heads = list(map(float, input().split()))

dp = [[0.0 for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0] = 1.0

for i in range(1, n + 1):
    for target in range(i + 1):
        if target > 0:
            dp[i][target] += p_heads[i - 1] * dp[i - 1][target - 1]
        dp[i][target] += (1 - p_heads[i - 1]) * dp[i - 1][target]

total_probability = sum(dp[n][i] for i in range(half + 1, n + 1))

print(total_probability)
