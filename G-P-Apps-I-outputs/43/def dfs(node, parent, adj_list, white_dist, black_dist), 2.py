
MOD = 10**9 + 7

def dfs(node, parent, adj_list, white_dist, black_dist):
    white_max = black_max = 0
    for child in adj_list[node]:
        if child == parent:
            continue

        dfs(child, node, adj_list, white_dist, black_dist)

        white_max = max(white_max, white_dist[child] + 1)
        black_max = max(black_max, black_dist[child] + 1)

    white_dist[node] = white_max
    black_dist[node] = black_max

def sum_niceness(N, edges):
    white_dist = [0] * (N + 1)
    black_dist = [0] * (N + 1)
    adj_list = [[] for _ in range(N + 1)]
    
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)

    dfs(1, 0, adj_list, white_dist, black_dist)

    total_niceness = 0
    for i in range(1, N + 1):
        total_niceness = (total_niceness + max(white_dist[i], black_dist[i])) % MOD

    return total_niceness

# Sample Input
N = 2
edges = [(1, 2)]

print(sum_niceness(N, edges))
```
