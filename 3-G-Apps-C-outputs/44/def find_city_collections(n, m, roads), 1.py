
def find_city_collections(n, m, roads):
    graph = [[] for _ in range(n)]
    for x, y in roads:
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)
    
    visited = [False] * n
    collection1 = []
    collection2 = []
    
    def dfs(node, collection):
        visited[node] = True
        collection.append(node+1)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, collection)
    
    dfs(0, collection1)
    dfs(1, collection2)
    
    for i in range(n):
        if not visited[i]:
            return "impossible"
    
    return f"{collection1[0]} {' '.join(map(str, collection1[1:]))}\n{collection2[0]} {' '.join(map(str, collection2[1:]))}"

# Input parsing
n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
print(find_city_collections(n, m, roads))
