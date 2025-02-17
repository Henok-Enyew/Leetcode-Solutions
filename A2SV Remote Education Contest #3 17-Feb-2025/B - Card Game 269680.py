# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B

from collections import Counter

cards = int(input())
card = list(map(int, input().split()))
sm = sum(card)
partition = int(sm / int(cards/2))
mp = Counter()
# print(sm, partition)
visited = []
for i in range(cards):
    for j in range(cards):
        if i not in visited and j not in visited and i!=j and card[i] + card[j] == partition:
            print(f"{i+1} {j+1}")
            visited.append(i)
            visited.append(j)
            continue