
MOD = 10**9 + 7

def dfs(u, p, g, d):
    for v in g[u]:
        if v != p:
            d[v] = d[u] + 1
            dfs(v, u, g, d)

def solve():
    N = int(input().strip())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]

    adj = [[] for _ in range(N)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    dist_white = [0] * N
    dist_black = [0] * N

    dfs(0, -1, adj, dist_white)
    max_dist_white = max(dist_white)

    max_dist_white_vertex = dist_white.index(max_dist_white)
    dfs(max_dist_white_vertex, -1, adj, dist_black)
    max_dist_black = max(dist_black)

    total_niceness = max(max_dist_white, max_dist_black) % MOD
    print(total_niceness)

solve()
