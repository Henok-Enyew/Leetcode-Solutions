# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

def generate_matrix(n):
    if n == 2:
        print(-1)
        return
    matrix = [[0] * n for _ in range(n)]
    odd_numbers = list(range(1, n*n + 1, 2))
    even_numbers = list(range(2, n*n + 1, 2))
    
    numbers = odd_numbers + even_numbers 
    index = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = numbers[index]
            index += 1
    for row in matrix:
        print(*row)
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    generate_matrix(n)
