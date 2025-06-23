# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

from collections import defaultdict
n,m = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    row = list(map(int, input().split()))
    graph[row[0]].append(row[1])
    graph[row[1]].append(row[0])
l = len(graph[1])
ans = 'YES'
for g in graph.keys():
    if len(graph[g]) != l:
        ans = 'NO'
print(ans)