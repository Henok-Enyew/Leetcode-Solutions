# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n,m = map(int, input().split())

for i in range(1,n+1):
    if i %2 != 0:
        for j in range(1,m+1):
            print("#", end="")
    else:
        for j in range(1,m+1):
            if i %4 == 2 and j == m:
                print("#", end="")
            elif i %4 == 0 and j == 1:
                print("#", end="")
            else:
                print(".", end="")
    print()
            