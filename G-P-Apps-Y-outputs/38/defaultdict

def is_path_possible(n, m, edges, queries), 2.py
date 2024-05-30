
from collections import defaultdict

def is_path_possible(n, m, edges, queries):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    parent = [-1] * (n + 1)
    
    def dfs(node, par):
        parent[node] = par
        for child in graph[node]:
            if child != par:
                dfs(child, node)
    
    dfs(1, -1)
    
    def is_valid_path(query):
        for v in query:
            if v == 1:
                continue
            if parent[v] == -1 or parent[v] in query:
                continue
            valid = False
            for u in query:
                if parent[v] == u or parent[u] == v:
                    valid = True
                    break
            if not valid:
                return False
        return True
    
    for query in queries:
        if is_valid_path(query):
            print("YES")
        else:
            print("NO")

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]
queries = [list(map(int, input().split()))[1:] for _ in range(m)]

is_path_possible(n, m, edges, queries)
