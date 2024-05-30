
import sys
from collections import defaultdict

def dfs(tree, root, parent, depth, ancestors):
    if parent == -1:
        depth[root] = 0
    else:
        depth[root] = depth[parent] + 1

    ancestors[root].append(root)
    for child in tree[root]:
        if child != parent:
            ancestors[child] = ancestors[root][:]
            dfs(tree, child, root, depth, ancestors)

def solve(n, m, edges, queries):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    depth = [0] * (n + 1)
    ancestors = defaultdict(list)
    dfs(tree, 1, -1, depth, ancestors)

    for query in queries:
        k = query[0]
        vertices = query[1:]
        min_depth = float('inf')
        for v in vertices:
            min_depth = min(min_depth, depth[v])

        has_common_ancestor = False
        for a in ancestors[1]:
            if all(v in ancestors[a] or depth[v] == depth[a] + 1 for v in vertices):
                has_common_ancestor = True
                break

        if min_depth <= depth[1] and not has_common_ancestor:
            print("NO")
        else:
            print("YES")

# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
queries = [list(map(int, input().split()[1:])) for _ in range(m)]

# Solve the problem
solve(n, m, edges, queries)
```
