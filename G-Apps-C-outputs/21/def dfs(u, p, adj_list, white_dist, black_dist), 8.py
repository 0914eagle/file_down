
MOD = 10**9 + 7

def dfs(u, p, adj_list, white_dist, black_dist):
    white_max = 0
    black_max = 0

    for v in adj_list[u]:
        if v == p:
            continue
        white_child, black_child = dfs(v, u, adj_list, white_dist, black_dist)
        white_max = max(white_max, white_child + 1)
        black_max = max(black_max, black_child + 1)

    white_dist[u] = white_max
    black_dist[u] = black_max
    return white_max, black_max

def sum_niceness(N, edges):
    adj_list = [[] for _ in range(N)]
    white_dist = [0] * N
    black_dist = [0] * N

    for a, b in edges:
        adj_list[a-1].append(b-1)
        adj_list[b-1].append(a-1)

    dfs(0, -1, adj_list, white_dist, black_dist)

    total_niceness = 0
    for i in range(N):
        total_niceness = (total_niceness + max(white_dist[i], black_dist[i])) % MOD

    return total_niceness

# Read input
N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

# Calculate and print the result
print(sum_niceness(N, edges))
