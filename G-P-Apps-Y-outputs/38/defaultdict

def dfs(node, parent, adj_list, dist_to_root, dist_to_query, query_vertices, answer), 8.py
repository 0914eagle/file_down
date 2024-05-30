
from collections import defaultdict

def dfs(node, parent, adj_list, dist_to_root, dist_to_query, query_vertices, answer):
    if node in query_vertices:
        dist_to_query[node] = 0
    elif parent != -1:
        dist_to_query[node] = dist_to_query[parent] + 1

    for neighbor in adj_list[node]:
        if neighbor == parent:
            continue
        dfs(neighbor, node, adj_list, dist_to_root, dist_to_query, query_vertices, answer)
        dist_to_root[node] = max(dist_to_root[node], dist_to_root[neighbor] + 1)

    if dist_to_query[node] <= dist_to_root[node]:
        answer[node] = True

n, m = map(int, input().split())
adj_list = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for _ in range(m):
    query = list(map(int, input().split()))[1:]
    dist_to_root = [0] * (n + 1)
    dist_to_query = [float('inf')] * (n + 1)
    answer = [False] * (n + 1)
    dfs(1, -1, adj_list, dist_to_root, dist_to_query, set(query), answer)
    
    if any(answer[v] for v in query):
        print("YES")
    else:
        print("NO")
