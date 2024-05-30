
MOD = 10**9 + 7

def dfs(vertex, parent, adj_list, white_dist, black_dist):
    white_dist[vertex] = 0
    black_dist[vertex] = 0
    
    for neighbor in adj_list[vertex]:
        if neighbor == parent:
            continue
        dfs(neighbor, vertex, adj_list, white_dist, black_dist)
        white_dist[vertex] = max(white_dist[vertex], white_dist[neighbor] + 1)
        black_dist[vertex] = max(black_dist[vertex], black_dist[neighbor] + 1)

def sum_niceness(N, edges):
    adj_list = [[] for _ in range(N+1)]
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    white_dist = [0] * (N+1)
    black_dist = [0] * (N+1)
    
    dfs(1, 0, adj_list, white_dist, black_dist)
    
    ans = 0
    for i in range(1, N+1):
        ans = (ans + max(white_dist[i], black_dist[i])) % MOD
    
    return ans

# Sample Input
N = 2
edges = [(1, 2)]

print(sum_niceness(N, edges))
