
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def dfs(node, parent, graph, values, result):
    max_beauty = values[node - 1]
    for neighbor in graph[node]:
        if neighbor != parent:
            neighbor_beauty = dfs(neighbor, node, graph, values, result)
            max_beauty = max(max_beauty, gcd(values[node - 1], neighbor_beauty))
    result[node - 1] = max_beauty
    return max_beauty

def solve_tree_beauty(n, values, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    result = [0] * n
    dfs(1, -1, graph, values, result)

    return ' '.join(map(str, result))

# Input
n = int(input())
values = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(n - 1)]

# Output
print(solve_tree_beauty(n, values, edges))
