# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

def can_unlock(password, words):
    first_letter_match = False
    second_letter_match = False

    for word in words:
        if word == password:  
            print("YES")
            return
        if word[1] == password[0]:  
            first_letter_match = True
        if word[0] == password[1]: 
            second_letter_match = True

    if first_letter_match and second_letter_match:
        print("YES")
    else:
        print("NO")

password = input().strip()
n = int(input().strip())
words = [input().strip() for _ in range(n)]

can_unlock(password, words)
