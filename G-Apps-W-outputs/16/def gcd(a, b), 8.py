
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def dfs(adj_list, values, node, parent):
    max_gcd = values[node-1]
    for child in adj_list[node]:
        if child != parent:
            child_gcd = dfs(adj_list, values, child, node)
            max_gcd = max(max_gcd, gcd(values[node-1], child_gcd))
    return max_gcd

def solve_tree_beauty(n, values, edges):
    adj_list = {i: [] for i in range(1, n+1)}
    for x, y in edges:
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    beauties = []
    for i in range(1, n+1):
        max_gcd = dfs(adj_list, values, i, parent=-1)
        beauties.append(max_gcd)
    
    return beauties

# Input parsing
n = int(input())
values = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(n-1)]

# Solve the problem
result = solve_tree_beauty(n, values, edges)

# Output the result
print(*result)
