
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def dfs(node, parent, graph, values, ans, max_gcd):
    current_value = values[node]
    current_gcd = gcd(current_value, max_gcd)
    ans[node] = max(current_gcd, ans[node])
    max_gcd = max(max_gcd, current_gcd)
    
    for child in graph[node]:
        if child != parent:
            dfs(child, node, graph, values, ans, max_gcd)

n = int(input())
values = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = [0] * (n+1)
dfs(1, 0, graph, values, ans, 0)

print(" ".join(map(str, ans[1:])))
