
MOD = 10**9 + 7

def dfs(u, p, adj_list, cnt):
    c = 1
    for v in adj_list[u]:
        if v == p:
            continue
        c += dfs(v, u, adj_list, cnt)
    cnt[u] = c
    return c

def niceness_sum(N, edges):
    adj_list = [[] for _ in range(N)]
    for a, b in edges:
        adj_list[a-1].append(b-1)
        adj_list[b-1].append(a-1)

    cnt = [0] * N
    dfs(0, -1, adj_list, cnt)

    ans = 0
    for u in range(N):
        ans = (ans + cnt[u] * (N - cnt[u])) % MOD

    return ans

# Reading input
N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]
print(niceness_sum(N, edges))
```
