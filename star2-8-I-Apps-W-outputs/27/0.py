
h, w = map(int, input().split())
r = list(map(int, input().split()))
c = list(map(int, input().split()))
MOD = 10**9 + 7
grid = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(c[i]):
        grid[i][j] = 1
for j in range(w):
    for i in range(r[j]):
        grid[i][j] = 1
ways = 1
for i in range(h):
    for j in range(w):
        if grid[i][j] == 1:
            ways *= 2
            ways %= MOD
print(ways)

