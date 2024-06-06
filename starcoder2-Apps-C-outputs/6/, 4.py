
import sys

sys.setrecursionlimit(10 ** 9)

n, m, k = map(int, input().split())

o = [0] * (n + 1)
c = [0] * (n + 1)

for i in map(int, input().split()):
    o[i] = 1

for i in map(int, input().split()):
    c[i] = 1

g = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    a, *b = map(int, input().split())
    g[i] = b

ans = 0

def dfs(v, col):
    global ans
    ans += 1
    for u in g[v]:
        if o[u] == col and c[u] == col:
            return True
        if o[u] == col or c[u] == col:
            if dfs(u, col):
                return True
    return False

if dfs(1, 1) and dfs(1, 0):
    print(ans)
else:
    print("impossible")
