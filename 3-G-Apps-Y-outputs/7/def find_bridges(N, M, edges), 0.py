
def find_bridges(N, M, edges):
    def dfs(u, p):
        nonlocal timer
        low[u] = disc[u] = timer
        timer += 1
        for v in graph[u]:
            if v == p:
                continue
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.add((u, v))
            else:
                low[u] = min(low[u], disc[v])

    graph = [[] for _ in range(N + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    disc = [-1] * (N + 1)
    low = [-1] * (N + 1)
    timer = 0
    bridges = set()

    dfs(1, -1)

    return len(bridges)

# Read input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# Find and print the number of bridges
print(find_bridges(N, M, edges))
