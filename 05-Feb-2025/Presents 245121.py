# Problem: Presents - https://codeforces.com/problemset/problem/136/A

t = int(input())
presents = list(map(int, input().split()))  
output = [0] * t  

for i in range(t):
    output[presents[i] - 1] = i + 1  

print(*output)  
