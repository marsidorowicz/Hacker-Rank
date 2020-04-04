#!/bin/python

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    x=y=0
    a1 = a[0]
    b1 = b[0]
    if a1>b1:
        x+=1
    elif a1<b1:
        y+=1
    else:
        pass
    a2 = a[1]
    b2 = b[1]
    if a2>b2:
        x+=1
    elif a2<b2:
        y+=1
    else:
        pass
    a3 = a[2]
    b3 = b[2]
    if a3>b3:
        x+=1
    elif a3<b3:
        y+=1
    else:
        pass
    result = [x, y]
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
