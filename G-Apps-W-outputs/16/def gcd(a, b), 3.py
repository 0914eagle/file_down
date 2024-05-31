
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def dfs(node, parent, graph, values, max_gcd):
    ans = values[node]
    for child in graph[node]:
        if child != parent:
            child_ans = dfs(child, node, graph, values, max_gcd)
            ans = max(ans, child_ans, gcd(values[node], child_ans))
    max_gcd[node] = ans
    return ans

def solve_tree_beauty(n, values, edges):
    graph = {i: [] for i in range(1, n+1)}
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    max_gcd = [0] * (n+1)
    dfs(1, -1, graph, values, max_gcd)
    
    return ' '.join(str(max_gcd[i]) for i in range(1, n+1))

# Input parsing
n = int(input())
values = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(n-1)]

# Output
print(solve_tree_beauty(n, values, edges))
