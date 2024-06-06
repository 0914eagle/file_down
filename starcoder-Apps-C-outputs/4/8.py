
# -*- coding: utf-8 -*-

# 1403

# 2021-04-27

# 1

N = int(input())

X = []
Y = []

for i in range(2*N):
    t = input().split()
    if t[0] == "B":
        X.append(int(t[1]))
    else:
        Y.append(int(t[1]))

X.sort()
Y.sort()

ans = 0

for i in range(N):
    ans += abs(X[i] - (i+1))
    ans += abs(Y[i] - (i+1))

print(ans)
