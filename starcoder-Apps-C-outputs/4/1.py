
#!/usr/bin/env python3
# https://abc088.contest.atcoder.jp/tasks/abc088_d

import sys

N = int(sys.stdin.readline())

data = []

for _ in range(N):
    data.append(list(sys.stdin.readline().rstrip()))

dp = [[-1] * N for _ in range(N)]
dp[0][0] = 1

dx = [1, 0]
dy = [0, 1]

for x in range(N):
    for y in range(N):
        if data[x][y] == '#':
            continue
        for i in range(2):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < N and y_ < N and dp[x_][y_] == -1:
                dp[x_][y_] = dp[x][y] + 1

if dp[N - 1][N - 1] == -1:
    print(-1)
else:
    num = N * N - sum(row.count('#') for row in data)
    print(num - dp[N - 1][N - 1] - 1)
