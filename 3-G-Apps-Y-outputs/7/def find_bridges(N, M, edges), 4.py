
def find_bridges(N, M, edges):
    def dfs(u, parent):
        nonlocal time
        low[u] = disc[u] = time
        time += 1
        for v in graph[u]:
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent:
                low[u] = min(low[u], disc[v])

    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    disc = [-1] * N
    low = [-1] * N
    time = 0
    bridges = []

    dfs(0, -1)

    return len(bridges)

# Read input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# Find and print the number of bridges
print(find_bridges(N, M, edges))
