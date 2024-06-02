
def find_collections(n, m, roads):
    adj_list = [[] for _ in range(n)]
    for x, y in roads:
        adj_list[x-1].append(y-1)
        adj_list[y-1].append(x-1)

    def bfs(start):
        visited = [False] * n
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

    arya_collection = bfs(0)
    sansa_collection = bfs(1)

    remaining_cities = set(range(n)) - set(arya_collection) - set(sansa_collection)

    for city in remaining_cities:
        if all(city in adj_list[other_city] for other_city in remaining_cities):
            arya_collection.append(city)
        else:
            sansa_collection.append(city)

    if len(arya_collection) + len(sansa_collection) == n:
        return arya_collection, sansa_collection
    else:
        return "impossible"

# Input
n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

# Output
result = find_collections(n, m, roads)
if result == "impossible":
    print("impossible")
else:
    arya_cities, sansa_cities = result
    print(" ".join(str(city+1) for city in arya_cities))
    print(" ".join(str(city+1) for city in sansa_cities))
