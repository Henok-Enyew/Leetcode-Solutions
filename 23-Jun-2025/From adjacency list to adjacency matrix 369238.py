# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    row = row[1:]
    mrow = [0] * n
    for r in row:
        mrow[r-1] = 1
    matrix.append(mrow)
for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]) + ' ' ,end="")
    print('')