#!/bin/python3
#https://www.hackerrank.com/challenges/30-operators/
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = round((meal_cost*(tip_percent/100)), 2)
    tax = round((meal_cost)*(tax_percent/100), 2)
    total = meal_cost+tip+tax
    print(int(total))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
