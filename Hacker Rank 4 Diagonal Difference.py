#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def check1(arr):
    i = j = m = key1 = key2 = p = value1 = value2 = val = 0
    result = 0
    for i in range(0, n):
        while j < n:
            key1 = j
            arr[key1] = arr[i][i]
            i += 1
            j += 1
            val = val + arr[key1]
    x = val
    return x


def check2(arr1):
    i = j = key1 = key2 = p = value1 = value2 = val = 0
    result = 0
    m = n
    while i < n:
        while j < n:
            key1 = j
            arr1[key1] = arr1[i][m - 1]
            i += 1
            j += 1
            m = m - 1
            val = val + arr1[key1]
    x = val
    return x


def diagonalDifference(arr):
    # Write your code here
    arr1 = list(arr)
    x = check1(arr)
    y = check2(arr1)

    result = abs(x - y)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
