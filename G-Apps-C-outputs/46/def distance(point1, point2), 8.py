
import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def solve_aqueduct(n, s, t, q, hills, springs, towns):
    def is_feasible(length):
        graph = {i: [] for i in range(n)}
        
        for i, spring_hill in enumerate(springs):
            graph[n+i] = []
            graph[spring_hill].append(n+i)
        
        for i, town_hill in enumerate(towns):
            graph[n+s+i] = []
            graph[town_hill].append(n+s+i)
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    d = distance(hills[i], hills[j])
                    if d <= length:
                        graph[i].append(j)
        
        def dfs(node, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
        
        visited_nodes = set()
        for node in range(n):
            if node not in visited_nodes:
                dfs(node, visited_nodes)
        
        for i in range(n, n+s):
            if i not in visited_nodes:
                return False
        
        return all(i in visited_nodes for i in range(n+s, n+s+t))
    
    left = 0
    right = 10**6
    eps = 1e-6
    
    while right - left > eps:
        mid = (left + right) / 2
        if is_feasible(mid):
            right = mid
        else:
            left = mid
    
    return right

# Input
n, s, t, q = map(int, input().split())
hills = [list(map(int, input().split())) for _ in range(n)]
springs = [int(x) for x in input().split()]
towns = [int(x) for x in input().split()]

# Output
result = solve_aqueduct(n, s, t, q, hills, springs, towns)
if result is False:
    print("IMPOSSIBLE")
else:
    print("{:.6f}".format(result))

