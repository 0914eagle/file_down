
def solve(n, m, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a-1].add(b-1)
        adj[b-1].add(a-1)
    def dfs(v, seen):
        seen.add(v)
        for w in adj[v]:
            if w not in seen:
                dfs(w, seen)
    dfs(0, set())
    return n - len(seen)

