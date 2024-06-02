
def find_bridges(N, M, edges):
    def dfs(u, p, timer):
        nonlocal bridges, tin, low
        visited[u] = True
        tin[u] = low[u] = timer
        timer += 1
        for v in graph[u]:
            if v == p:
                continue
            if not visited[v]:
                dfs(v, u, timer)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    bridges.add((u, v))
            else:
                low[u] = min(low[u], tin[v])

    graph = [[] for _ in range(N + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N + 1)
    tin = [0] * (N + 1)
    low = [0] * (N + 1)
    bridges = set()
    dfs(1, -1, 0)

    return len(bridges)

# Read input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# Find and print the number of bridges
print(find_bridges(N, M, edges))
