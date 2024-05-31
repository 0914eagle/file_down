
import math

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def dfs(node, parent, tree, numbers, gcd_values):
    max_gcd = 0
    for child in tree[node]:
        if child != parent:
            max_gcd = max(max_gcd, dfs(child, node, tree, numbers, gcd_values))
    gcd_values[node] = numbers[node - 1]
    for child in tree[node]:
        if child != parent:
            gcd_values[node] = find_gcd(gcd_values[node], gcd_values[child])
    return max(gcd_values[node], max_gcd)

def solve_tree_beauty(n, numbers, edges):
    tree = {i: [] for i in range(1, n+1)}
    for x, y in edges:
        tree[x].append(y)
        tree[y].append(x)
    
    gcd_values = [0] * (n+1)
    dfs(1, 0, tree, numbers, gcd_values)
    
    return ' '.join(str(gcd_values[i]) for i in range(1, n+1))

# Input parsing
n = int(input())
numbers = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(n-1)]

# Output
print(solve_tree_beauty(n, numbers, edges))
