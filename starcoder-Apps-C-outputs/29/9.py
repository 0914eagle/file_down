
import numpy as np

n = int(input())

xs, ys = [], []
for i in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

ans = 0
for i in range(n):
    if i == 0:
        xs_i, xs_j = xs[-1], xs[0]
        ys_i, ys_j = ys[-1], ys[0]
    else:
        xs_i, xs_j = xs[i-1], xs[i]
        ys_i, ys_j = ys[i-1], ys[i]

    area = abs(xs_i*ys_j - xs_j*ys_i) / 2
    ans += area * (abs(xs_i) + abs(xs_j) + abs(ys_i) + abs(ys_j))

ans /= sum([abs(xs[i]*ys[i+1] - xs[i+1]*ys[i]) for i in range(n-1)])
print(ans)
