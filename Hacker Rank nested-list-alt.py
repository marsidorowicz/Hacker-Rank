from decimal import Decimal
from itertools import groupby, islice
from operator import itemgetter

xx = []
for i in range(int(input())):
  x, y = (input(), Decimal(input()))
  xx.append((y, x))
xx.sort()
for k, v in islice(groupby(xx, key=itemgetter(0)), 1, 2):
  for x in v:
    print(x[1])
