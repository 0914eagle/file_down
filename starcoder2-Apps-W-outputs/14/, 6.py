
n = int(input())

graph = [[] for _ in range(n)]

for _ in range(n-1):
    a, b, z = map(int, input().split())
    graph[a-1].append((b-1, z))
    graph[b-1].append((a-1, z))

order = list(map(int, input().split()))

def dfs(node, parent, xor_sum):
    boring_pairs = 0
    for child, z in graph[node]:
        if child != parent:
            boring_pairs += dfs(child, node, xor_sum ^ z)
    if xor_sum == 0:
        boring_pairs += 1
    print(boring_pairs)
    return boring_pairs

for i in order:
    dfs(i, -1, 0)
