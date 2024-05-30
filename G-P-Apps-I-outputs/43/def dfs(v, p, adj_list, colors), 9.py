
MOD = 10**9 + 7

def dfs(v, p, adj_list, colors):
    white_dist = 0
    black_dist = 0
    for u in adj_list[v]:
        if u == p:
            continue
        w, b = dfs(u, v, adj_list, colors)
        white_dist = max(white_dist, w + (colors[u] == 1))
        black_dist = max(black_dist, b + (colors[u] == 0))
    return white_dist, black_dist

def solve_tree_painting(N, edges):
    adj_list = [[] for _ in range(N)]
    for a, b in edges:
        adj_list[a-1].append(b-1)
        adj_list[b-1].append(a-1)
        
    ans = 0
    for mask in range(1 << N):
        colors = [(mask >> i) & 1 for i in range(N)]
        white_dist, black_dist = dfs(0, -1, adj_list, colors)
        ans = (ans + max(white_dist, black_dist)) % MOD
    
    return ans

# Sample Input
N = 2
edges = [(1, 2)]

print(solve_tree_painting(N, edges))
```
