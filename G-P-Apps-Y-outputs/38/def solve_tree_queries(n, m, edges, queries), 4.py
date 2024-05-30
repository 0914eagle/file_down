
from collections import deque

def solve_tree_queries(n, m, edges, queries):
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(node, parent, query_vertices):
        if node in query_vertices:
            return True
        for child in graph[node]:
            if child != parent:
                if dfs(child, node, query_vertices):
                    return True
        return False

    for query in queries:
        k = query[0]
        query_vertices = set(query[1:])
        root = 1
        q = deque()
        q.append((root, 0))
        while q:
            node, parent = q.popleft()
            if dfs(node, parent, query_vertices):
                print("YES")
                break
            for child in graph[node]:
                if child != parent:
                    q.append((child, node))
        else:
            print("NO")

# Input parsing
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(n-1)]
queries = [list(map(int, input().split()))[1:] for _ in range(m)]

# Solve the queries
solve_tree_queries(n, m, edges, queries)
