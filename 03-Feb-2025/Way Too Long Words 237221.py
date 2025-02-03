# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

t = int(input())
while(t > 0):
    t -= 1
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        print(f"{word[0]}{len(word)-2}{word[len(word)-1]}")