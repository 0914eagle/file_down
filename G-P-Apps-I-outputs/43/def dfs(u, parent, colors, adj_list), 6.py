
MOD = 10**9 + 7

def dfs(u, parent, colors, adj_list):
    max_dist_white = 0
    max_dist_black = 0
    
    for v in adj_list[u]:
        if v != parent:
            child_max_dist_white, child_max_dist_black = dfs(v, u, colors, adj_list)
            max_dist_white = max(max_dist_white, 1 + child_max_dist_white)
            max_dist_black = max(max_dist_black, 1 + child_max_dist_black)
    
    if colors[u] == 0:
        return max_dist_white, max_dist_black
    elif colors[u] == 1:
        return max_dist_white, 0
    else:
        return 0, max_dist_black

def sum_niceness(N, edges):
    adj_list = [[] for _ in range(N)]
    for a, b in edges:
        adj_list[a-1].append(b-1)
        adj_list[b-1].append(a-1)
    
    ans = 0
    for mask in range(1 << N):
        colors = [(mask >> i) & 1 for i in range(N)]
        niceness = max(dfs(0, -1, colors, adj_list))
        ans = (ans + niceness) % MOD
    
    return ans

# Input parsing
N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

# Call the function with the input
print(sum_niceness(N, edges))
