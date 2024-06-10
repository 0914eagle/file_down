
n = int(input())
a = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    v, u = map(int, input().split())
    v, u = v - 1, u - 1
    graph[v].append(u)
    graph[u].append(v)
def dfs(v, p = -1):
    size = 1
    is_red = (a[v] == 1)
    is_blue = (a[v] == 2)
    for u in graph[v]:
        if u == p:
            continue
        child_size, child_is_red, child_is_blue = dfs(u, v)
        size += child_size
        is_red |= child_is_red
        is_blue |= child_is_blue
    return size, is_red, is_blue
total_size = n
total_is_red = (1 in a)
total_is_blue = (2 in a)
count = 0
for v in range(n):
    size, is_red, is_blue = dfs(v)
    if not (is_red and is_blue):
        count += 1
print(count)

