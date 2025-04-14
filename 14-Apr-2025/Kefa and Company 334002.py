# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B

n, d = map(int, input().split())
friends = []
for _ in range(n):
    m, s = map(int, input().split())
    friends.append((m, s))

friends.sort()
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + friends[i][1]

max_friendship = 0
left = 0
for right in range(n):
    while friends[right][0] - friends[left][0] >= d:
        left += 1
    current_sum = prefix[right+1] - prefix[left]
    if current_sum > max_friendship:
        max_friendship = current_sum

print(max_friendship)