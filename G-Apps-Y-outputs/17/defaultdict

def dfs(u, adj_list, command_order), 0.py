
from collections import defaultdict

def dfs(u, adj_list, command_order):
    command_order.append(u)
    for v in adj_list[u]:
        dfs(v, adj_list, command_order)

def process_query(n, q, adj_list, queries):
    result = []
    for u, k in queries:
        command_order = []
        dfs(u, adj_list, command_order)
        if k <= len(command_order):
            result.append(command_order[k-1])
        else:
            result.append(-1)
    return result

n, q = map(int, input().split())
superiors = list(map(int, input().split()))
adj_list = defaultdict(list)
for i, superior in enumerate(superiors, start=2):
    adj_list[superior].append(i)

queries = []
for _ in range(q):
    u, k = map(int, input().split())
    queries.append((u, k))

results = process_query(n, q, adj_list, queries)
for res in results:
    print(res)
