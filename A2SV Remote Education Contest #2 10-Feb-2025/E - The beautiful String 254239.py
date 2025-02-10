# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

def is_1100(target, j):
    return target[j:j+4] == ['1', '1', '0', '0']

test = int(input())
for test_round in range(test):
    target = list(input().strip())
    len_target = len(target)
    iter_count = int(input())

    count = sum(1 for j in range(len_target - 3) if is_1100(target, j))

    for round in range(iter_count):
        i, q = input().split()
        i = int(i) - 1

        if target[i] == q:
            print("YES" if count > 0 else "NO")
            continue

        for j in range(max(0, i - 3), min(i + 1, len_target - 3)):
            if is_1100(target, j):
                count -= 1

        target[i] = q

        for j in range(max(0, i - 3), min(i + 1, len_target - 3)):
            if is_1100(target, j):
                count += 1

        print("YES" if count > 0 else "NO")
