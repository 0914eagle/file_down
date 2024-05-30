
from collections import defaultdict

def solve_tree_queries(n, m, edges, queries):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)

    def dfs(node, par, dep):
        parent[node] = par
        depth[node] = dep
        for nei in graph[node]:
            if nei != par:
                dfs(nei, node, dep + 1)
    
    dfs(1, 0, 0)

    def is_valid_path(u, vertices):
        for v in vertices:
            if depth[v] <= depth[u] + 1 and parent[v] != u and parent[u] != v:
                return False
        return True

    for query in queries:
        k = query[0]
        vertices = query[1:]
        valid = False
        for u in vertices:
            if is_valid_path(u, vertices):
                valid = True
                break
        if valid:
            print("YES")
        else:
            print("NO")

# Input parsing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]
queries = [list(map(int, input().split()))[1:] for _ in range(m)]

# Call the function with the input data
solve_tree_queries(n, m, edges, queries)
