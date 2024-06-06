
import numpy as np

n = int(input())

if n == 2:
    print("1 2 1")
    exit()

res = []
number = 1
for i in range(2, n):
    res.append([1, i, number])

res.append([1, 2, number+1])
number += 1

for i in range(3, n+1):
    res.append([2, i, number])

print("\n".join([" ".join(map(str, item)) for item in res]))
