
MOD = 10**9 + 7

def dfs(node, parent, graph, white_dist, black_dist):
    white_dist[node] = 0
    black_dist[node] = 0

    for child in graph[node]:
        if child == parent:
            continue
        dfs(child, node, graph, white_dist, black_dist)
        white_dist[node] = max(white_dist[node], white_dist[child] + 1)
        black_dist[node] = max(black_dist[node], black_dist[child] + 1)

def solve():
    N = int(input())
    graph = {i: [] for i in range(1, N + 1)}
    white_dist = [0] * (N + 1)
    black_dist = [0] * (N + 1)

    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1, -1, graph, white_dist, black_dist)

    total_niceness = 0
    for i in range(1, N + 1):
        total_niceness = (total_niceness + max(white_dist[i], black_dist[i])) % MOD

    print(total_niceness)

solve()
