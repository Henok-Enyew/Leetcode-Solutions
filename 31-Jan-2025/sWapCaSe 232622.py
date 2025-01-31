# Problem: sWapCaSe - https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    output = ''
    for st in s:
        if st.islower():
            output+=st.upper()
        else:
            output+=st.lower()
    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)