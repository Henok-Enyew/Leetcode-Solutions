# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def get_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(limit + 1) if sieve[i]]

primes = get_primes(55)

n = int(input())

count = 0
for num in range(1, n + 1):
    temp = num
    prime_divs = 0

    for p in primes:
        if temp < p:
            break
        if temp % p == 0:
            prime_divs += 1
            while temp % p == 0:
                temp //= p

    if temp > 1:
        prime_divs += 1
    if prime_divs == 2:
        count += 1

print(count)