
def maximize_profit(N, M, A, B, edges):
    graph = {}
    for i in range(1, N+1):
        graph[i] = []
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(node, visited):
        visited.add(node)
        total_cost = A[node-1]
        total_score = B[node-1]

        for neighbor in graph[node]:
            if neighbor not in visited:
                cost, score = dfs(neighbor, visited)
                total_cost += cost
                total_score += score
        
        return total_cost, total_score
    
    profit = 0
    visited = set()
    for i in range(1, N+1):
        if i not in visited:
            cost, score = dfs(i, visited)
            profit = max(profit, abs(score) - cost)
    
    return profit

# Input parsing
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Call the function and print the result
print(maximize_profit(N, M, A, B, edges))
```
