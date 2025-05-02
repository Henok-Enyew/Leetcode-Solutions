# Problem: Convert a String to an Integer using Recursion - https://www.geeksforgeeks.org/convert-a-string-to-an-integer-using-recursion/

def stringToIntHelper(str, index):
    if index == len(str):
        return 0
    digit = int(str[index])
    return digit * (10 ** (len(str) - index - 1)) + stringToIntHelper(str, index + 1)
def stringToInt(str):
    return stringToIntHelper(str, 0)