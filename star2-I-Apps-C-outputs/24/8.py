
def solve(n, edges):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for u, v in edges:
        graph[u - 1][v - 1] = 1
        graph[v - 1][u - 1] = 1
    
    def dfs(u, color):
        visited[u] = color
        for v in range(n):
            if graph[u][v] and not visited[v]:
                dfs(v, 3 - color)
    
    visited = [0 for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            dfs(u, 1)
    
    def check_string(s):
        for u in range(n):
            for v in range(n):
                if graph[u][v] != (abs(ord(s[u]) - ord(s[v])) == 1):
                    return False
        return True
    
    for i in range(n):
        s = 'a' * i + 'b' + 'a' * (n - i - 1)
        if check_string(s):
            return 'Yes\n' + s
    
    for i in range(n):
        s = 'a' * i + 'c' + 'a' * (n - i - 1)
        if check_string(s):
            return 'Yes\n' + s
    
    return 'No'

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(solve(n, edges))

