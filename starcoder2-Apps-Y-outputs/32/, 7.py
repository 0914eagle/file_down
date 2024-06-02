
n = int(input())

edges = [[] for i in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

def dfs(v, p):
    global ans, a, b, c
    if len(edges[v]) == 1:
        ans = 1
        a = v
        b = p
        c = p
        return
    for u in edges[v]:
        if u == p:
            continue
        dfs(u, v)
        if ans + 1 > ans:
            ans += 1
            a = v
            b = u
            c = p

ans = 0
dfs(0, -1)
print(ans)
print(a + 1, b + 1, c + 1)


a, b = map(int, input().split())
print(a + b)

