# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

def main():
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    abc = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [[0] * 3 for _ in range(N)]
    dp[0][0], dp[0][1], dp[0][2] = abc[0]

    for i in range(1, N):
        a, b, c = abc[i]
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + b
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + c

    print(max(dp[N-1]))

if __name__ == "__main__":
    main()
