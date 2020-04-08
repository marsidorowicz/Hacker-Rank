n = int(input())
arr = input()
lis = list(map(int, arr.split()))
a, b = -1, -1
for i in lis:
    if (i > a):
        a, b = i, a
    elif (i < a and i > b):
        b = i
print (n)