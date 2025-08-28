# Problem: G - Longest Path - https://atcoder.jp/contests/dp/tasks/dp_g

import sys
from collections import deque

sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    g = [[] for _ in range(N)]
    indeg = [0]*N
    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        g[x].append(y)
        indeg[y] += 1
    q = deque([i for i in range(N) if indeg[i] == 0])
    dp = [0]*N
    while q:
        u = q.popleft()
        for v in g[u]:
            if dp[v] < dp[u] + 1:
                dp[v] = dp[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    print(max(dp))

if __name__ == "__main__":
    main()
