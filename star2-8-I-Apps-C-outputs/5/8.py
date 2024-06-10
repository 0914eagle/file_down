
def dfs(node, parent, depth):
    global marked
    if depth >= D:
        marked[node] = True
    for child in tree[node]:
        if child != parent:
            dfs(child, node, depth+1)


N, D = map(int, input().split())
tree = [[] for _ in range(N)]
for i in range(1, N):
    x = int(input())
    tree[i].append(x)
    tree[x].append(i)

marked = [False] * N
dfs(0, -1, 0)
print(sum(marked))

