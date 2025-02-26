# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

t = int(input())

stack = []
store = set()
while t:
    t-=1
    friend = input()
    stack.append(friend)

for i in range(len(stack)-1,-1,-1):
    if not stack[i] in store:
        print(stack[i])
        store.add(stack[i])
