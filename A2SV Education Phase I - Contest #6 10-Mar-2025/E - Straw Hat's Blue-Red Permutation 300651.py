# Problem: E - Straw Hat's Blue-Red Permutation - https://codeforces.com/gym/594356/problem/E

import sys

def can_form_permutation(n, a, colors):
    red, blue = [], []
    for i in range(n):
        if colors[i] == 'R':
            red.append(a[i])
        else:
            blue.append(a[i])

    red.sort(reverse=True)
    blue.sort()

    for i in range(len(blue)):
        if blue[i] < i + 1:
            return "NO"

    for i in range(len(red)):
        if red[i] > n - i:
            return "NO"

    return "YES"

def main():
    t = int(sys.stdin.readline().strip())  
    results = []

    for _ in range(t):
        n = int(sys.stdin.readline().strip()) 
        a = list(map(int, sys.stdin.readline().split())) 
        colors = sys.stdin.readline().strip() 

        results.append(can_form_permutation(n, a, colors))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
