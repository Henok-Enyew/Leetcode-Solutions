# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

arrays = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        if arrays[i][j] == 1:
            row = i+1
            column = j+1
moves = abs(row-3) + abs(column-3)
print(moves)