# Problem: Team - https://codeforces.com/contest/231/problem/A

t = int(input())
questions_answered = 0
while(t > 0):
    t -= 1
    team = input().split()
    sures = 0
    for i in team:
        if i == '1':
            sures+=1
    if sures >= 2:
        questions_answered += 1
print(questions_answered)