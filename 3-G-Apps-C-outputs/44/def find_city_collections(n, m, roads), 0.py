
def find_city_collections(n, m, roads):
    adj_list = [[] for _ in range(n+1)]
    for road in roads:
        x, y = road
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    visited = [False] * (n+1)
    collection1 = []
    collection2 = []
    
    def dfs(node, collection):
        visited[node] = True
        collection.append(node)
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor, collection)
    
    dfs(1, collection1)
    dfs(2, collection2)
    
    for i in range(1, n+1):
        if not visited[i]:
            collection1.append(i)
    
    if len(collection1) + len(collection2) == n:
        print(" ".join(map(str, collection1)))
        print(" ".join(map(str, collection2)))
    else:
        print("impossible")

# Input
n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]

# Function call
find_city_collections(n, m, roads)
