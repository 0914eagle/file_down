
MOD = 10**9 + 7

def find_max_distances(node, parent, color, adj_list, white_dist, black_dist):
    if color == 0:
        white_dist[node] = 0
    else:
        black_dist[node] = 0

    for child in adj_list[node]:
        if child == parent:
            continue
        find_max_distances(child, node, 1-color, adj_list, white_dist, black_dist)
        if color == 0:
            white_dist[node] = max(white_dist[node], 1 + white_dist[child])
        else:
            black_dist[node] = max(black_dist[node], 1 + black_dist[child])

def sum_niceness_of_painting(N, edges):
    adj_list = [[] for _ in range(N+1)]
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)

    white_dist = [0] * (N+1)
    black_dist = [0] * (N+1)

    find_max_distances(1, -1, 0, adj_list, white_dist, black_dist)

    total_niceness = 0
    for i in range(1, N+1):
        total_niceness = (total_niceness + max(white_dist[i], black_dist[i])) % MOD

    return total_niceness

# Sample Input
N = 2
edges = [(1, 2)]
print(sum_niceness_of_painting(N, edges))
