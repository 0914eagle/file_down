
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    for u in graph:
        for v in graph[u]:
            out_degree[u] += 1
            in_degree[v] += 1
    
    max_count = 0
    for u in graph:
        if in_degree[u] == out_degree[u]:
            max_count += 1
    
    print(max_count)
    
    for u in graph:
        for v in graph[u]:
            print(u, v)

t = int(input())
for _ in range(t):
    solve()


