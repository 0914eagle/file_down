
def process_query(n, p, u, k):
    adj = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        adj[p[i-2]].append(i)
    
    order = []
    def dfs(node):
        order.append(node)
        for child in adj[node]:
            dfs(child)
    
    dfs(u)
    
    if k > len(order):
        return -1
    else:
        return order[k-1]

n, q = map(int, input().split())
p = list(map(int, input().split()))

for _ in range(q):
    u, k = map(int, input().split())
    result = process_query(n, p, u, k)
    print(result)
