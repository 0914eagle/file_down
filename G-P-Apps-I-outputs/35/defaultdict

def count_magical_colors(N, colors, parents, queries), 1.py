
from collections import defaultdict

def count_magical_colors(N, colors, parents, queries):
    tree = defaultdict(list)
    for i in range(1, N):
        tree[parents[i-1]].append(i)

    def dfs(node):
        count = defaultdict(int)
        count[colors[node]] = 1

        for child in tree[node]:
            child_count = dfs(child)
            for color, color_count in child_count.items():
                count[color] += color_count

        magical_colors = 0
        for color, color_count in count.items():
            if color_count % 2 == 1:
                magical_colors += 1

        return count

    results = []
    for query in queries:
        if query[0] == 0:
            results.append(dfs(query[1])[colors[query[1]]])
        else:
            colors[query[1]] = query[0]

    return results

# Input parsing
N, Q = map(int, input().split())
colors = list(map(int, input().split()))
parents = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

result = count_magical_colors(N, colors, parents, queries)

for res in result:
    print(res)
```
