
MOD = 10**9 + 7

def dfs(v, p, adj_list, white_max_distance, black_max_distance):
    white_distances = []
    black_distances = []
    
    for u in adj_list[v]:
        if u == p:
            continue
        white_dist, black_dist = dfs(u, v, adj_list, white_max_distance, black_max_distance)
        white_distances.append(white_dist)
        black_distances.append(black_dist)
    
    if len(white_distances) == 0:
        white_max_distance[v] = 0
    else:
        white_max_distance[v] = max(white_distances) + 1
    
    if len(black_distances) == 0:
        black_max_distance[v] = 0
    else:
        black_max_distance[v] = max(black_distances) + 1
    
    return white_max_distance[v], black_max_distance[v]

def sum_niceness(N, edges):
    adj_list = {i: [] for i in range(1, N+1)}
    
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    white_max_distance = [0] * (N+1)
    black_max_distance = [0] * (N+1)
    
    dfs(1, -1, adj_list, white_max_distance, black_max_distance)
    
    total_niceness = sum(max(white_max_distance[v], black_max_distance[v]) for v in range(1, N+1)) % MOD
    return total_niceness

# Sample Input
N = 2
edges = [(1, 2)]

print(sum_niceness(N, edges))
