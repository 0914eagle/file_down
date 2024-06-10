
import sys
from collections import defaultdict
from heapq import heappush, heappop

def solve(n, m, p, insecure, connections):
    graph = defaultdict(list)
    for x, y, l in connections:
        graph[x].append((y, l))
        graph[y].append((x, l))
    
    min_cost = 0
    visited = set()
    pq = [(0, 1)]
    
    while pq:
        cost, node = heappop(pq)
        
        if node in visited:
            continue
        
        visited.add(node)
        min_cost += cost
        
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heappush(pq, (edge_cost, neighbor))
    
    if len(visited) == n and all(node not in insecure for node in visited):
        return min_cost
    
    return "impossible"

def main():
    n, m, p = map(int, input().split())
    insecure = set(map(int, input().split()))
    connections = [tuple(map(int, input().split())) for _ in range(m)]
    
    result = solve(n, m, p, insecure, connections)
    
    print(result)

if __name__ == "__main__":
    main()

