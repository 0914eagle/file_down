
from math import ceil
n,r,p = [int(i) for i in input().split()]
t = ceil(r/p)
if n == 1:
    print(0)
elif n-t > 0:
    print(p*(n-t))
else:
    print(0)

