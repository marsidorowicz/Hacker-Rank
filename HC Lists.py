# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
#
# Input Format
#
# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.
#
# Constraints
#
# The elements added to the list must be integers.
# Output Format
#
# For each command of type print, print the list on a new line.
#
# Sample Input 0
#
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0
#
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

if __name__ == '__main__':
    l = []
    N = int(input())
    for i in range(N):
        command = list(map(str, input().rstrip().split()))
        if 'insert' in command:
            l.insert(int(command[1]), int(command[2]))
        if 'print' in command:
            print(l)
        if 'remove' in command:
            l.remove(int(command[1]))
        if 'append' in command:
            l.append(int(command[1]))
        if 'sort' in command:
            l.sort()
        if 'pop' in command:
            l.pop()
        if 'reverse' in command:
            l.reverse()