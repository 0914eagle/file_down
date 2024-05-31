
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def dfs(node, parent, nums, graph, ans):
    curr_gcd = nums[node-1]
    for child in graph[node]:
        if child == parent:
            continue
        child_gcd = dfs(child, node, nums, graph, ans)
        curr_gcd = gcd(curr_gcd, child_gcd)
    ans[node-1] = curr_gcd
    return curr_gcd

def max_beauty(n, nums, edges):
    graph = {i: [] for i in range(1, n+1)}
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    ans = [0] * n
    dfs(1, -1, nums, graph, ans)
    
    return ans

# Input parsing
n = int(input())
nums = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(n-1)]

# Calculate and output the maximum possible beauty of each vertex
result = max_beauty(n, nums, edges)
print(*result)
