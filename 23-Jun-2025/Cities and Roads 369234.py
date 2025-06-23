# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())
count = 0
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(0, len(row)):
        if row[j] == 1:
            count += 1
print(int(count/2))