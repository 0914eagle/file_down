
def process_query(n, p, u, k):
    graph = [[] for _ in range(n)]
    for i in range(1, n):
        graph[p[i-2] - 1].append(i)
    
    order = []
    def dfs(node):
        order.append(node)
        for child in graph[node]:
            dfs(child)
    
    dfs(u - 1)
    
    if k > len(order):
        return -1
    return order[k - 1] + 1

# Input parsing
n, q = map(int, input().split())
p = list(map(int, input().split()))

# Process queries
for _ in range(q):
    u, k = map(int, input().split())
    result = process_query(n, p, u, k)
    print(result)
