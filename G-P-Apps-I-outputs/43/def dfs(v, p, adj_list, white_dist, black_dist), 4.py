
MOD = 10**9 + 7

def dfs(v, p, adj_list, white_dist, black_dist):
    white_dist[v] = 0
    black_dist[v] = 0
    for u in adj_list[v]:
        if u == p:
            continue
        dfs(u, v, adj_list, white_dist, black_dist)
        white_dist[v] = max(white_dist[v], white_dist[u] + 1)
        black_dist[v] = max(black_dist[v], black_dist[u] + 1)

def sum_niceness(N, edges):
    adj_list = [[] for _ in range(N)]
    for a, b in edges:
        adj_list[a-1].append(b-1)
        adj_list[b-1].append(a-1)

    white_dist = [0] * N
    black_dist = [0] * N

    dfs(0, -1, adj_list, white_dist, black_dist)

    total_niceness = 0
    for i in range(N):
        total_niceness += max(white_dist[i], black_dist[i])

    return total_niceness % MOD

# Input
N = 2
edges = [[1, 2]]

# Output
print(sum_niceness(N, edges))
```
