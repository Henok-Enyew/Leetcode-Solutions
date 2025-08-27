# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

def main():
    import sys
    input = sys.stdin.readline
    
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    dp = [float('inf')] * N
    dp[0] = 0

    for i in range(1, N):
        for j in range(1, K + 1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + abs(h[i] - h[i - j]))
    
    print(dp[N - 1])

if __name__ == "__main__":
    main()
