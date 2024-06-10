
def solve(n, edges):
    graph = {i: set() for i in range(1, n+1)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    def dfs(node, seen, letter):
        seen.add(node)
        for neighbour in graph[node]:
            if neighbour not in seen:
                dfs(neighbour, seen, letter)
    
    seen = set()
    dfs(1, seen, 'a')
    
    if len(seen) == n:
        return 'Yes\n' + ''.join(['a'] * n)
    
    seen = set()
    dfs(1, seen, 'b')
    
    if len(seen) == n:
        return 'Yes\n' + ''.join(['b'] * n)
    
    seen = set()
    dfs(1, seen, 'c')
    
    if len(seen) == n:
        return 'Yes\n' + ''.join(['c'] * n)
    
    return 'No'

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(solve(n, edges))

