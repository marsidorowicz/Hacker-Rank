#https://www.hackerrank.com/challenges/designer-door-mat/
# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
#N, M = input().split()
N = 11
M = 33
N = int(N)
M = int(M)
mark = ".|."
text = "WELCOME"

for i in range(0, N):
    if i<N//2:
        for j in range(1, M-1-6*i):
            if j==((M//2)-2*i-i):
                print((mark*2*i)+mark, end="")
            else:
                print("-", end="")
        print("")
    if i==N//2:
        for j in range(0, M-6):
            if j==((M//2)-3):
                print(text, end="")
            else:
                print("-", end="")
        print("")
    if N>i>N//2:
        y = (N//2+1)
        x = abs(y-i)+1
        x1 = abs(y-1)
        x2 = abs(y-i)
        z = N//2-i+1
        z1 = N//2-i
        z2 = N-i-1
        for j in range(1, M-1-2*z2*3):
            if j==(M//2-3*z2):
                print((mark*2*z2)+mark, end="")
                #print(mark+(2*mark), end="")
                #print(((((N-2)+2*z)*mark)), end="")
            else:
                print("-", end="")
        print("")

