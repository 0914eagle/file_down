
MOD = 10**9 + 7

def dfs(v, p, d, cnt):
    cnt[v] += 1
    for u in edges[v]:
        if u == p:
            continue
        dfs(u, v, d + 1, cnt)
        cnt[v] = max(cnt[v], cnt[u] + 1)

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

black_count = [0] * N
white_count = [0] * N

dfs(0, -1, 0, black_count)

p = edges[0][0]
dfs(p, 0, 0, white_count)

total = 0
for i in range(N):
    total = (total + max(white_count[i], black_count[i])) % MOD

print(total)
```
