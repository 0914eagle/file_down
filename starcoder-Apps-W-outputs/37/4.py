
from math import log10

x, y = map(int, input().split())

if x == 1 and y == 1:
    print(0)
elif x == 1 and y != 1:
    print('Impossible')
else:
    val = 10**(y-1)
    print(10**y - val)
