
def process_query(n, p, u, k):
    adj_list = [[] for _ in range(n + 1)]
    for i, parent in enumerate(p, start=2):
        adj_list[parent].append(i)

    def dfs(node):
        order.append(node)
        for child in adj_list[node]:
            dfs(child)

    order = []
    dfs(u)
    if k > len(order):
        return -1
    return order[k - 1]

n, q = map(int, input().split())
p = list(map(int, input().split()))

for _ in range(q):
    u, k = map(int, input().split())
    result = process_query(n, p, u, k)
    print(result)
