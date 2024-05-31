
MOD = 10**9 + 7

def dfs(node, parent, adj_list, white_dist, black_dist):
    white_dist[node] = 0
    black_dist[node] = 0
    
    for child in adj_list[node]:
        if child == parent:
            continue
        dfs(child, node, adj_list, white_dist, black_dist)
        
        white_dist[node] = max(white_dist[node], white_dist[child] + 1)
        black_dist[node] = max(black_dist[node], black_dist[child] + 1)

def solve_tree_painting(N, edges):
    adj_list = [[] for _ in range(N+1)]
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    white_dist = [0] * (N+1)
    black_dist = [0] * (N+1)
    
    dfs(1, 0, adj_list, white_dist, black_dist)
    
    total_niceness = 0
    for i in range(1, N+1):
        total_niceness = (total_niceness + max(white_dist[i], black_dist[i])) % MOD
    
    return total_niceness

# Read input
N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

# Call the function and print the result
print(solve_tree_painting(N, edges))
