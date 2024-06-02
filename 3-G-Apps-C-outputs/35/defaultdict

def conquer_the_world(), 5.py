
import sys
from collections import defaultdict

def conquer_the_world():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
        graph[v].append((u, c))
    
    armies = []
    for _ in range(n):
        x, y = map(int, input().split())
        armies.append((x, y))
    
    def dfs(node, parent):
        total_cost = 0
        for neighbor, cost in graph[node]:
            if neighbor != parent:
                total_cost += dfs(neighbor, node) + min(armies[neighbor-1][0], armies[neighbor-1][1]) * cost
        return total_cost
    
    total_cost = dfs(1, -1)
    print(total_cost)

conquer_the_world()
