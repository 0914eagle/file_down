
def solve(n, a, edges):
    adj = [[] for _ in range(n)]
    for v, u in edges:
        v, u = v - 1, u - 1
        adj[v].append(u)
        adj[u].append(v)
    def dfs(u, p, red, blue):
        if a[u] == 1:
            red += 1
        elif a[u] == 2:
            blue += 1
        for v in adj[u]:
            if v != p:
                red, blue = dfs(v, u, red, blue)
        return red, blue
    return sum(dfs(u, -1, 0, 0)[0] * dfs(u, -1, 0, 0)[1] for u in range(n))

