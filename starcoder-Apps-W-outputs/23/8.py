
from random import *
from math import *

n, m = 10**5, 2*10**5
print(n, m)

S = [i for i in range(1,n+1)]

for i in range(m):
    u = choice(S)
    S.remove(u)
    v = choice(S)
    S.remove(v)
    print(u,v)
