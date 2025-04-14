# Problem: D - Urbanization - https://codeforces.com/gym/603156/problem/D

n, n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

if n1 > n2:
    n1, n2 = n2, n1

sum1 = sum(a[:n1])
sum2 = sum(a[n1:n1 + n2])
result = (sum1 / n1) + (sum2 / n2)

print("{0:.8f}".format(result))