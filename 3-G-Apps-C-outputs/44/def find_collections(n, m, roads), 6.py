
def find_collections(n, m, roads):
    adj_list = [[] for _ in range(n+1)]
    for road in roads:
        x, y = road
        adj_list[x].append(y)
        adj_list[y].append(x)

    def bfs(start):
        visited = [False] * (n+1)
        queue = [start]
        visited[start] = True
        collection = [start]

        while queue:
            node = queue.pop(0)
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    collection.append(neighbor)

        return collection

    arya_collection = bfs(1)
    sansa_collection = bfs(2)

    remaining_cities = set(range(1, n+1)) - set(arya_collection) - set(sansa_collection)

    for city in remaining_cities:
        if all(city in adj_list[other_city] for other_city in remaining_cities if other_city != city):
            arya_collection.append(city)
        else:
            sansa_collection.append(city)

    if len(arya_collection) + len(sansa_collection) == n:
        print(" ".join(map(str, arya_collection)))
        print(" ".join(map(str, sansa_collection)))
    else:
        print("impossible")

# Input parsing
n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

find_collections(n, m, roads)
