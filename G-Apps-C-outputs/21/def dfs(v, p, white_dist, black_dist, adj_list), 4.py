
MOD = 10**9 + 7

def dfs(v, p, white_dist, black_dist, adj_list):
    white_max_dist = 0
    black_max_dist = 0
    
    for u in adj_list[v]:
        if u == p:
            continue
        
        white_child, black_child = dfs(u, v, white_dist, black_dist, adj_list)
        
        white_max_dist = max(white_max_dist, white_child + 1)
        black_max_dist = max(black_max_dist, black_child + 1)
    
    if white_max_dist == 0:
        white_max_dist = white_dist[v]
    if black_max_dist == 0:
        black_max_dist = black_dist[v]
    
    return white_max_dist, black_max_dist

N = int(input())
adj_list = [[] for _ in range(N)]
white_dist = [0] * N
black_dist = [0] * N

for i in range(N-1):
    a, b = map(int, input().split())
    adj_list[a-1].append(b-1)
    adj_list[b-1].append(a-1)

for i in range(N):
    white_dist[i] = len(adj_list[i]) - 1
    black_dist[i] = len(adj_list[i]) - 1

total_niceness = 0

for i in range(N):
    white_max, black_max = dfs(i, -1, white_dist, black_dist, adj_list)
    total_niceness += max(white_max, black_max)

print(total_niceness % MOD)
