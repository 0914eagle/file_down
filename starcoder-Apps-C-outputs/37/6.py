
import numpy as np
import pandas as pd
import itertools

n, m = map(int,input().split())

ships = []

for _ in range(m):
    a, b, c = map(int,input().split())
    for i in range(a,b+1):
        ships.append((i,c))

ships = set(ships)

for i in range(-n,n):
    if (i,n) not in ships:
        print("-"*i+"0"+"-"*(n-1-i))
        break
else:
    print("impossible")
