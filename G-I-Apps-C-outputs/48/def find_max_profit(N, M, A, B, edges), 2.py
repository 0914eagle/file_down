
def find_max_profit(N, M, A, B, edges):
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    def dfs(node, visited):
        visited.add(node)
        local_score = abs(B[node])
        for neighbor in graph[node]:
            if neighbor not in visited:
                local_score += dfs(neighbor, visited)
        return local_score

    max_profit = 0
    for i in range(N):
        visited = set()
        local_score = dfs(i, visited)
        profit = local_score - A[i]
        max_profit = max(max_profit, profit)

    return max_profit

# Reading input
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]

# Calling the function and printing the result
print(find_max_profit(N, M, A, B, edges))
