# Problem: A - Nathan is rich - https://codeforces.com/gym/588094/problem/A

t = int(input())
while t:
    t-=1
    wheels = int(input())
    minimum_wheels = wheels//4
    if wheels%4!=0:
        minimum_wheels+=1
    print(minimum_wheels)