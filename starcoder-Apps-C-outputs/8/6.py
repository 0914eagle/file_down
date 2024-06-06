
from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
p = list(map(int, input().split()))
r = list(map(int, input().split()))

P = [[0]*m for _ in range(m)]
for i in range(m):
    for j in range(m):
        if i == j: continue
        P[i][j] = max(p[i], r[j])

dp = [[-1]*(n+1) for _ in range(m)]
for i in range(m):
    dp[i][1] = 1

Q = deque()
Q.append((1, 0, 0))
while Q:
    t, i, j = Q.popleft()
    for k in range(m):
        if t+P[j][k] <= n and dp[k][t+P[j][k]] < dp[i][t] + 1:
            dp[k][t+P[j][k]] = dp[i][t] + 1
            Q.append((t+P[j][k], i, k))

print(max([max(x) for x in dp]))
