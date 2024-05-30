
def cross_river(P, R, L, logs):
    graph = {}
    for i in range(-2, R):
        graph[i] = []
    
    for log in logs:
        graph[log[0]].append(log[1])
        graph[log[1]].append(log[0])
    
    visited = set()
    people_left = P
    
    def dfs(node):
        nonlocal people_left
        if node == -1:
            people_left -= 1
            return
        
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    dfs(-2)
    
    if people_left == 0:
        return P * 2
    else:
        return people_left

# Sample Input
P, R, L = 2, 4, 7
logs = [(-2, 0), (0, -1), (-2, 1), (1, 0), (2, 1), (2, 3), (3, -1)]

result = cross_river(P, R, L, logs)
print(result)
