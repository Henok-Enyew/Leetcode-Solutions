# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

n = int(input())
for i in range(n):
    row = list(map(int, input().split()))
    count = 0
    vertices = ""
    for j in range(0, len(row)):
        if row[j] == 1:
            count += 1
            vertices = vertices + str(j+1) + " " 
    print(str(count) + ' '+ vertices)