# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
array = list(map(int, input().split()))
window_sum = 0
left = 0
max_len = 0
for right in range(n):
    window_sum+=array[right]
    while window_sum > s :
        window_sum -= array[left]
        left+=1
    max_len = max(max_len, right-left+1)
print(max_len)    

