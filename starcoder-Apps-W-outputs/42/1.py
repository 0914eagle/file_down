

from itertools import permutations
from copy import deepcopy

n = int(input())
x, y, z = [], [], []
for i in range(n):
    x_i, y_i, z_i = map(int, input().split())
    x.append(x_i)
    y.append(y_i)
    z.append(z_i)

orig_x = deepcopy(x)
orig_y = deepcopy(y)
orig_z = deepcopy(z)

for idx in permutations(range(n)):
    x = deepcopy(orig_x)
    y = deepcopy(orig_y)
    z = deepcopy(orig_z)
    prev = []
    for i in range(n):
        x[idx[i]], y[idx[i]], z[idx[i]] = x[i], y[i], z[i]
    for i in range(n):
        p = []
        for j in range(i + 1, n):
            if (min(x[i], x[j]) <= x[prev] <= max(x[i], x[j]) and min(y[i], y[j]) <= y[prev] <= max(y[i], y[j]) and min(z[i], z[j]) <= z[prev] <= max(z[i], z[j])):
                break
            p.append(j)
        prev = p[0]
        print(idx[i] + 1, idx[prev] + 1)
