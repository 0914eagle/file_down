
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    d = {}
    for i, x in enumerate(arr, 1):
        if x not in d:
            d[x] = [i]
        else:
            d[x].append(i)
    
    graph = {i: [] for i in range(1, n+1)}
    
    for k, v in d.items():
        v = sorted(v)
        for i in range(1, len(v)):
            graph[v[i-1]].append(v[i])
            graph[v[i]].append(v[i-1])
    
    queue = [1]
    visited = set()
    while queue:
        node = queue.pop(0)
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    if len(visited) == n:
        print("YES")
        for k, v in graph.items():
            if len(v) > 1:
                print(k, v[0])
    else:
        print("NO")

