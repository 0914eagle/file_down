
def count_magical_colors(N, Q, colors, parent_nodes, queries):
    tree = [[] for _ in range(N+1)]
    for i in range(2, N+1):
        tree[parent_nodes[i-1]].append(i)
    
    def dfs(node):
        counts = [0] * 101
        counts[colors[node]] = 1
        for child in tree[node]:
            child_counts = dfs(child)
            for i in range(1, 101):
                counts[i] += child_counts[i]
        return counts
    
    counts = dfs(1)
    
    result = []
    for k, x in queries:
        if k == 0:
            result.append(counts[x])
        else:
            counts[x] = 0
            colors[x] = k
            counts = dfs(1)
    
    return result

# Input parsing
N, Q = map(int, input().split())
colors = [0] + list(map(int, input().split()))
parent_nodes = [0] + list(map(int, input().split()))
queries = []
for _ in range(Q):
    k, x = map(int, input().split())
    queries.append((k, x))

result = count_magical_colors(N, Q, colors, parent_nodes, queries)
for res in result:
    print(res)
```
