
from math import log
for _ in range(int(input())):
    n,l,r = map(int,input().split())
    if n == 0:
        print(0)
    else:
        m = int(log(n, 2))
        l = m+1-l
        r = m+1-r
        print(r-l+1)
