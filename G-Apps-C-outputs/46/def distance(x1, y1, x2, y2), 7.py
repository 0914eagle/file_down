
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def dfs(current, target, visited, graph, springs, towns, q):
    if current == target:
        return True
    
    visited[current] = True
    
    for neighbor, length in graph[current]:
        if not visited[neighbor] and length <= q and dfs(neighbor, target, visited, graph, springs, towns, q):
            return True
    
    return False

def build_graph(n, hills, springs, towns):
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, h1 = hills[i]
            x2, y2, h2 = hills[j]
            length = distance(x1, y1, x2, y2) + abs(h2 - h1)
            graph[i].append((j, length))
            graph[j].append((i, length))
    
    for spring in springs:
        for town in towns:
            visited = [False] * n
            if not dfs(spring - 1, town - 1, visited, graph, springs, towns, q):
                return None
    
    return graph

def solve_problem():
    n, s, t, q = map(int, input().split())
    hills = [list(map(int, input().split())) for _ in range(n)]
    springs = list(map(int, input().split()))
    towns = list(map(int, input().split()))
    
    graph = build_graph(n, hills, springs, towns)
    
    if graph is None:
        print("IMPOSSIBLE")
    else:
        total_length = sum(min(edge[1] for edge in graph[node]) for node in range(n))
        print("{:.6f}".format(total_length))

# Input parsing
solve_problem()
