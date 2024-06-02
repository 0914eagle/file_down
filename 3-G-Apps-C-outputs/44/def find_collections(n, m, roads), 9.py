
def find_collections(n, m, roads):
    adj_list = [[] for _ in range(n)]
    for road in roads:
        x, y = road
        adj_list[x-1].append(y-1)
        adj_list[y-1].append(x-1)

    visited = [False] * n
    collection1 = []
    collection2 = []

    def dfs(node, collection):
        visited[node] = True
        collection.append(node+1)
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor, collection)

    dfs(0, collection1)
    dfs(1, collection2)

    if len(collection1) + len(collection2) == n:
        print(' '.join(map(str, collection1)))
        print(' '.join(map(str, collection2)))
    else:
        print('impossible')

# Sample Input Parsing
n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

find_collections(n, m, roads)
