
import sys
from collections import defaultdict

def count_magical_colors(N, colors, parents, queries):
    graph = defaultdict(list)
    for i in range(1, N):
        graph[parents[i-1]].append(i)

    def dfs(node, color_count):
        color_count[colors[node]] += 1
        result = sum(val % 2 == 1 for val in color_count.values())
        for child in graph[node]:
            result += dfs(child, color_count.copy())
        color_count[colors[node]] -= 1
        return result

    results = []
    for query in queries:
        k, x = query
        if k == 0:
            color_count = defaultdict(int)
            result = dfs(x, color_count)
            results.append(result)
        else:
            colors[x] = k

    return results

# Read input
N, Q = map(int, input().split())
colors = list(map(int, input().split()))
parents = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

# Get results
results = count_magical_colors(N, colors, parents, queries)

# Print output
for result in results:
    print(result)
```
