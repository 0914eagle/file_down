
MOD = 10**9 + 7

def dfs(node, parent, graph):
    white_dist = 0
    black_dist = 0

    for child in graph[node]:
        if child == parent:
            continue

        child_white_dist, child_black_dist = dfs(child, node, graph)

        white_dist = max(white_dist, child_white_dist + 1)
        black_dist = max(black_dist, child_black_dist + 1)

    return white_dist, black_dist

N = int(input())
graph = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

white_dist, black_dist = dfs(0, -1, graph)

result = max(white_dist, black_dist) % MOD
print(result)
```
