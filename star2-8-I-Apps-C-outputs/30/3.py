
import sys
def readline():
    return sys.stdin.readline().strip()
def readint():
    return int(sys.stdin.readline().strip())
def readarray(type=int):
    return list(map(type, sys.stdin.readline().split()))
from itertools import product
n, q = readarray()
ops = [readline().split() for _ in range(q)]
res = 0
for s in product('abcdef', repeat=n):
    s = ''.join(s)
    for a, b in ops:
        while s[:2] == a:
            s = b + s[2:]
    if s == 'a':
        res += 1
print(res)

