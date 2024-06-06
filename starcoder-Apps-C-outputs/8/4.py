
from collections import defaultdict, Counter
import itertools
import math
import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

N, M = LI()
A = LI()
B = LI()
P = [[-1] * M for _ in range(N)]
for i in range(N):
    C, T = LI()
    C -= 1
    T -= 1
    P[i][C] = T

que = []
for i in range(M):
    que.append((A[i], i))
que.sort()
Q = [0] * M
for i in range(M):
    Q[que[i][1]] = i

# カット
for i in range(M):
    for j in range(M-1, Q[i]-1, -1):
        P[i].insert(0, -1)

ans = 0
for i in range(N):
    f = True
    for j in range(M):
        if P[i][j] >= 0:
            f = False
            break
    if not f:
        continue

    for j in range(M):
        if P[i][j] >= 0:
            P[i][j] += B[Q[j]]
            if j+1 < M:
                P[i][j+1] = P[i][j] - A[Q[j+1]]

    ans += 1
    P[i][0] = -1

print(ans)
