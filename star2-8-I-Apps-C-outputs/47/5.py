
from sys import stdin
from itertools import groupby

n, m = map(int, input().split())
x = {}
for i in range(n):
    s, pos = map(float, input().split())
    x[pos] = int(s)
species = [x[i] for i in sorted(x)]
replanted = 0
for k, g in groupby(species):
    if len(list(g)) > 1:
        replanted += len(list(g)) - 1
print(replanted)

