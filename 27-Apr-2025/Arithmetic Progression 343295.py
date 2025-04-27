# Problem: Arithmetic Progression - https://codeforces.com/problemset/problem/382/C

n = int(input())
a = list(map(int, input().split()))
a.sort()

if n == 1:
    print(-1)
else:
    diffs = []
    for i in range(1, n):
        diffs.append(a[i] - a[i-1])
    
    if len(set(diffs)) == 1:
        d = diffs[0]
        if d == 0:
            print(1)
            print(a[0])
        else:
            if n == 2:
                if d % 2 == 0:
                    mid = a[0] + d // 2
                    res = [a[0] - d, mid, a[-1] + d]
                    res = list(sorted(set(res)))
                    print(len(res))
                    print(' '.join(map(str, res)))
                else:
                    res = [a[0] - d, a[-1] + d]
                    res = list(sorted(set(res)))
                    print(len(res))
                    print(' '.join(map(str, res)))
            else:
                res = [a[0] - d, a[-1] + d]
                res = list(sorted(set(res)))
                print(len(res))
                print(' '.join(map(str, res)))
    else:
        freq = {}
        for diff in diffs:
            if diff in freq:
                freq[diff] += 1
            else:
                freq[diff] = 1
        if len(freq) > 2:
            print(0)
        else:
            keys = sorted(freq.keys())
            if len(keys) == 1:
                d = keys[0]
                if n == 2:
                    if d % 2 == 0:
                        mid = a[0] + d // 2
                        res = [a[0] - d, mid, a[-1] + d]
                        res = list(sorted(set(res)))
                        print(len(res))
                        print(' '.join(map(str, res)))
                    else:
                        res = [a[0] - d, a[-1] + d]
                        res = list(sorted(set(res)))
                        print(len(res))
                        print(' '.join(map(str, res)))
                else:
                    res = [a[0] - d, a[-1] + d]
                    res = list(sorted(set(res)))
                    print(len(res))
                    print(' '.join(map(str, res)))
            else:
                d1, d2 = keys
                if freq[d2] == 1 and d2 == 2 * d1:
                    pos = -1
                    for i in range(1, n):
                        if a[i] - a[i-1] == d2:
                            pos = i
                            break
                    num = a[pos-1] + d1
                    new_a = a.copy()
                    new_a.insert(pos, num)
                    valid = True
                    for i in range(1, len(new_a)):
                        if new_a[i] - new_a[i-1] != d1:
                            valid = False
                            break
                    if valid:
                        print(1)
                        print(num)
                    else:
                        print(0)
                else:
                    print(0)