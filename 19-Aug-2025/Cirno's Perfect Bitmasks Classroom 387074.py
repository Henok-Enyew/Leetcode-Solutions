# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
while t:
    t -= 1
    n = int(input())
    if n == 1:
        print(3)
    elif n & (n - 1) == 0: 
        print(n + 1)
    else:
        print(n & -n)  