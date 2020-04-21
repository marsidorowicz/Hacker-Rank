# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#
# For Example:
#
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
# Input Format
#
# A single line containing a string .
#
# Constraints
#
#
# Output Format
#
# Print the modified string .
#
# Sample Input 0
#
# HackerRank.com presents "Pythonist 2".
# Sample Output 0
#
# hACKERrANK.COM PRESENTS "pYTHONIST 2".
def swap_case(s):
    # result = ''
    # for char in s:
    #     if char.isupper():
    #         x = str(char.lower)
    #         result += x
    #     if char.islower():
    #         x = str(char.upper)
    #         result += x
    x = ''
    for char in s:
        if char.isupper():
            char = char.lower()
            x += char
        elif char.islower():
            char = char.upper()
            x += char
        else:
            x += char
    result = x
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#ALT
string_input = input()
print(string_input.swapcase())