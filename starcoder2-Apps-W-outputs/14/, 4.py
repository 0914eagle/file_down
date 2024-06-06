
# 100%

n = int(input())

tree = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b, z = map(int, input().split())
    tree[a].append((b, z))
    tree[b].append((a, z))

order = list(map(int, input().split()))

ans = [0] * n

def dfs(node, parent, xor):
    ans[node - 1] = 1 if xor == 0 else 0
    for child, z in tree[node]:
        if child != parent:
            dfs(child, node, xor ^ z)

dfs(1, 0, 0)

for i in order:
    a, b, z = tree[i][0]
    tree[i].pop(0)
    tree[a].remove((i, z))
    tree[b].remove((i, z))
    dfs(a, 0, z)
    dfs(b, 0, z)

for i in ans:
    print(i)
