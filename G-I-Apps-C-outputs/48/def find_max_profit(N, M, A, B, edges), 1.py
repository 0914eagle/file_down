
def find_max_profit(N, M, A, B, edges):
    graph = {i+1: {'cost': A[i], 'value': B[i], 'neighbors': []} for i in range(N)}
    for u, v in edges:
        graph[u]['neighbors'].append(v)
        graph[v]['neighbors'].append(u)
    
    def dfs(node, visited):
        visited.add(node)
        component_cost = graph[node]['cost']
        component_value = graph[node]['value']
        for neighbor in graph[node]['neighbors']:
            if neighbor not in visited:
                neighbor_cost, neighbor_value = dfs(neighbor, visited)
                component_cost += neighbor_cost
                component_value += neighbor_value
        return component_cost, component_value
    
    visited = set()
    profit = 0
    for node in range(1, N+1):
        if node not in visited:
            component_cost, component_value = dfs(node, visited)
            profit = max(profit, abs(component_value) - component_cost)
    
    return profit

# Read input
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Find and print the maximum profit
print(find_max_profit(N, M, A, B, edges))
```
