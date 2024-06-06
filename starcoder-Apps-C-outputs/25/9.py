
from copy import deepcopy

def dfs(x, y, n):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and M[nx][ny] == 1:
                dfs(nx, ny, n)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
M = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = 0
for i in range(m):
    r, c = map(int, input().split())
    M[r][c] = 1

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and M[i][j] == 1:
            dfs(i, j, n)
            ans += 1
print(ans)
