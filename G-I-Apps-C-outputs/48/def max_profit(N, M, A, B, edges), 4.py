
def max_profit(N, M, A, B, edges):
    def dfs(v, visited):
        visited[v] = True
        score = abs(B[v])
        for u in edges[v]:
            if not visited[u]:
                score += dfs(u, visited)
        return score
    
    max_profit = float("-inf")
    for i in range(N):
        visited = [False] * N
        profit = abs(sum(B)) - A[i] + dfs(i, visited)
        max_profit = max(max_profit, profit)
    
    return max_profit

# Input
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
edges = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

# Output
print(max_profit(N, M, A, B, edges))
