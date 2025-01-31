# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t = int(input())
while(t > 0):
    t -= 1
    story = input()
    codeforces = "codeforces"
    counter = 0
    
    for i in range(10):
        if story[i] != codeforces[i]:
            counter += 1

    print(counter)