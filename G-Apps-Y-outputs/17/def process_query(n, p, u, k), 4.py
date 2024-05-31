
def process_query(n, p, u, k):
    graph = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        graph[p[i-2]].append(i)
    
    order = [u]
    stack = [u]
    while stack:
        curr = stack.pop()
        for child in sorted(graph[curr]):
            order.append(child)
            stack.append(child)
    
    if k <= len(order):
        return order[k-1]
    else:
        return -1

n, q = map(int, input().split())
p = list(map(int, input().split()))

for _ in range(q):
    u, k = map(int, input().split())
    print(process_query(n, p, u, k))
