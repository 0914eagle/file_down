
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def dfs(node, parent, values, graph, result):
    max_gcd = values[node - 1]
    
    for child in graph[node]:
        if child != parent:
            child_gcd = dfs(child, node, values, graph, result)
            max_gcd = max(max_gcd, gcd(values[node - 1], child_gcd))
    
    result[node - 1] = max_gcd
    return max_gcd

def max_beauty(n, values, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    result = [0] * n
    dfs(1, -1, values, graph, result)
    
    return result

# Reading input
n = int(input())
values = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(n - 1)]

# Calculate and print output
output = max_beauty(n, values, edges)
print(*output)
