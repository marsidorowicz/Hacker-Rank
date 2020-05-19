# Objective
# Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!
#
# Task
# Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.
#
# Input Format
#
# A single integer, .
#
# Constraints
#
# Output Format
#
# Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .
#
# Sample Input 1
#
# 5
# Sample Output 1
#
# 1
# Sample Input 2
#
# 13
# Sample Output 2
#
# 2
# Explanation
#
# Sample Case 1:
# The binary representation of  is , so the maximum number of consecutive 's is .
#
# Sample Case 2:
# The binary representation of  is , so the maximum number of consecutive 's is .

#!/bin/python3

import math
import os
import random
import re
import sys

lst = []


def count_1(n):
    if len(n) == 1:
        if n == '1':
            x = 1
        else:
            x = 0
        return x
    else:
        if '1' in n:
            x = 1
            lst.append(x)
            for i in range(len(n)):
                if n[i] == '1':
                    x = 1
                    lst.append(x)
                    try:
                        while n[i+1] == '1':
                            x += 1
                            lst.append(x)
                            i += 1
                    except Exception:
                        pass
            print(lst)
            return max(lst)
        else:
            x = 0
            return x


if __name__ == '__main__':
    # n = int(input())
    n = 1112
    x = 0
    n = "{0:b}".format(n)
    print(n)
    x = count_1(n)
    print(x)