
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def dfs(node, parent, beauty, max_beauty, graph, numbers):
    max_beauty[node] = beauty
    for child in graph[node]:
        if child != parent:
            new_beauty = gcd(beauty, numbers[child])
            dfs(child, node, new_beauty, max_beauty, graph, numbers)

def solve_tree_beauty(n, numbers, edges):
    graph = [[] for _ in range(n+1)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    max_beauty = [0] * (n+1)
    dfs(1, 0, numbers[1], max_beauty, graph, numbers)
    
    return max_beauty[1:]

# Read input
n = int(input())
numbers = [0] + list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(n-1)]

# Solve and print output
result = solve_tree_beauty(n, numbers, edges)
print(*result)
