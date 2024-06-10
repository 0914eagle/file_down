
from collections import defaultdict


def solve(n, m, cities, roads):
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
    
    degree = defaultdict(int)
    
    for u in range(1, n+1):
        degree[u] = len(graph[u])
    
    can_orient = []
    
    for u in range(1, n+1):
        if degree[u] == 0:
            continue
        can_orient.append((u, graph[u][0]))
        degree[u] -= 1
        degree[graph[u][0]] += 1
    
    if all(degree[u] == 0 for u in range(1, n+1)):
        return can_orient
    
    return -1


if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        roads = []
        
        for _ in range(m):
            u, v = map(int, input().split())
            roads.append((u, v))
        
        result = solve(n, m, n, roads)
        
        if result == -1:
            print(-1)
        else:
            print(len(result))
            for u, v in result:
                print(u, v)

