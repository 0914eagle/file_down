
n = int(input())
edges = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

def dfs(v, p, d):
    max_d = d
    max_v = v
    for u in edges[v]:
        if u != p:
            new_d, new_v = dfs(u, v, d+1)
            if new_d > max_d:
                max_d = new_d
                max_v = new_v
    return max_d, max_v

def dfs2(v, p, d):
    max_d = d
    max_v = v
    for u in edges[v]:
        if u != p:
            new_d, new_v = dfs2(u, v, d+1)
            if new_d > max_d:
                max_d = new_d
                max_v = new_v
    return max_d, max_v

d1, v1 = dfs(0, -1, 0)
d2, v2 = dfs(v1, -1, 0)
d3, v3 = dfs2(v2, -1, 0)
d4, v4 = dfs2(v3, -1, 0)

print(d2+d4)
print(v2+1, v3+1, v4+1)

