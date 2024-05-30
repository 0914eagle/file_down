
from collections import defaultdict

def build_tree(n, edges):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    return tree

def dfs(tree, parent, node, query_vertices, query_set, result):
    if node in query_set:
        query_set.remove(node)
    for child in tree[node]:
        if child != parent:
            if dfs(tree, node, child, query_vertices, query_set, result):
                result.append(node)
    return node in query_vertices or len(query_set) > 0

def solve_tree_queries(n, m, edges, queries):
    tree = build_tree(n, edges)
    for query in queries:
        k, *vertices = query
        query_set = set(vertices)
        result = []
        dfs(tree, 0, 1, vertices, query_set, result)
        if len(result) > 0:
            print("YES")
        else:
            print("NO")

# Input processing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]
queries = [list(map(int, input().split()))[1:] for _ in range(m)]

# Solve queries
solve_tree_queries(n, m, edges, queries)
