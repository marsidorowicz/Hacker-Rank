#!/bin/python

import math
import os
import random
import re
import sys


# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    n = k = x = v = 0
    for k in range(0, len(ar)):
        while n < len(ar):
            key = n
            value = ar[n]
            v = value
            x = x + v
            n += 1
            k += 1
    return x
    result = x
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(long, raw_input().rstrip().split())

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
